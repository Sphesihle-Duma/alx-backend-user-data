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
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths):
            return True
        striped_path = path.rstrip('/')
        for exclude_path in excluded_paths:
            path_in_list = exclude_path.rstrip('/')
            if striped_path == path_in_list:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        '''Authorization function
        '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''' The current user to be authorized
        '''
        return None
