#!/usr/bin/env python3
''' authentication module
'''
import bcrypt


def _hash_password(password: str) -> bytes:
    ''' Hashing the password
    '''
    if password:
        b_password = password.encode('utf-8')
        salted = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(b_password, salted)
        return hashed_password
