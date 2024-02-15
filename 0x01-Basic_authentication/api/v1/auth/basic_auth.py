#!/usr/bin/env python3
''' basic authentication module
'''
from api.v1.auth.auth import Auth
from base64 import b64encode, b64decode


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        ''' validating the Base64 string
        '''
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = b64decode(base64_authorization_header)
            if b64encode(decoded) == base64_authorization_header.encode():
                return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        ''' finding user credentials in a decoded string
        '''
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        splited = decoded_base64_authorization_header.split(':')
        return (splited[0], splited[1])

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        '''finding user based on the email
           password
        '''
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
