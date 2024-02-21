#!/usr/bin/env python3
''' authentication module
'''
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    ''' Hashing the password
    '''
    if password:
        b_password = password.encode('utf-8')
        salted = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(b_password, salted)
        return hashed_password


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
