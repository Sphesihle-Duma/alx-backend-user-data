#!/usr/bin/env python3
''' basic authentication module
'''
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    ''' Basic authentication class
    '''
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        ''' extracting authorization header in the request
        '''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        splited = authorization_header.split()
        if splited[0] != 'Basic':
            return None
        return splited[1]
