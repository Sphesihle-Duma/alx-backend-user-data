#!/usr/bin/env python3
'''
   Authentication module
'''
from flask import request
from typing import List, TypeVar
import os


class Auth:
    ''' Authentication class

    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''require authorization function
        '''
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        striped_path = path.rstrip('/')
        for exclude_path in excluded_paths:
            path_in_list = exclude_path.rstrip('/')
            if path_in_list.endswith('*'):
                if striped_path.startswith(path_in_list[:-1]):
                    return False
            else:
                if striped_path == path_in_list:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        '''Authorization function
        '''
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        ''' The current user to be authorized
        '''
        return None

    def session_cookie(self, request=None):
        '''return cookie value
        '''
        if request is None:
            return None
        cookie_session = os.environ.get('SESSION_NAME', '_my_session_id')
        return request.cookies.get(cookie_session)
