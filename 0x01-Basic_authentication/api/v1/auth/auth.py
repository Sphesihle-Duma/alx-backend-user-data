#!/usr/bin/env python3
'''
   Authentication module
'''
from flask import request
from typing import List, TypeVar


class Auth:
    ''' Authentication class

    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''require authorization function
        '''
        return False

    def authorization_header(self, request=None) -> str:
        '''Authorization function
        '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''' The current user to be authorized
        '''
        return None
