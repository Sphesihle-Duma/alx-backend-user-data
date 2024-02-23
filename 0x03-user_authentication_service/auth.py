#!/usr/bin/env python3
''' authentication module
'''
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    ''' Hashing the password
    '''
    if password:
        b_password = password.encode('utf-8')
        salted = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(b_password, salted)
        return hashed_password


def _generate_uuid() -> str:
    '''
       Generating uuid
    '''
    return str(uuid.uuid4())


class Auth:
    '''Auth class to interact with the authentication database.
    '''

    def __init__(self):
        '''
           Constructor to initialised instance
           variables
        '''
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:

        '''
           Registering the user in the database
        '''
        if email and password:
            try:
                if self._db.find_user_by(email=email):
                    raise ValueError(f'User {email} already exists')
            except NoResultFound:
                hashed_passwd = _hash_password(password)
                return self._db.add_user(email, hashed_passwd)

    def valid_login(self, email: str, password: str) -> bool:
        '''
           validating credentials
        '''
        try:
            b_passwd = password.encode('utf-8')
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(b_passwd, user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        '''
           creating a session for a user
           Args:
              email: user's email
           return:
              session id
        '''
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        ''' returning a user from a session id
        '''
        if not isinstance(session_id, str):
            return None
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            if user:
                return user
            return None
        except Exception:
            return None
