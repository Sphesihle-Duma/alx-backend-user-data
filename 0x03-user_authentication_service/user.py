#!/usr/bin/env python3
'''
   user module
      this defines a User model
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    '''
       Defining a user model
    '''
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(
            self, email: str, hashed_password: str,
            session_id: str = None, reset_token: str = None):
        ''' A constructor
        '''
        self.email = email
        self.hashed_password = hashed_password
        self.reset_token = reset_token
        self.session_id = session_id
