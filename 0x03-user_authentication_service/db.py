#!/usr/bin/env python3
"""DB module
"""
import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB():
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        ''' adding a user to the database
           args
              email: user's email
              hashed_password: user's password
           Return
              User object
        '''
        new_session = self._session
        user = User(email, hashed_password)
        new_session.add(user)
        new_session.commit()
        return user

    def find_user_by(self, **kwargs):
        '''
          finding the user using keywords
        '''
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound
            return user
        except InvalidRequestError:
            raise

    def update_user(self, user_id: int, **kwargs) -> None:
        ''' Updating user based on user_id
        '''
        try:
            user = self.find_user_by(id=user_id)
        except Exception:
            raise
        try:
            update_data = {getattr(User, key): value for key, value in kwargs.items()}
            self._session.query(User).filter(User.id == user_id).update(update_data)
            self._session.commit()
        except ValueError:
            raise
