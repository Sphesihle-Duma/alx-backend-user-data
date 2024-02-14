from flask import request
''' authentication module
'''


class Auth:
    '''
       authentication class
    '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
           public class for authentication
        '''
        return False


    def authorization_header(self, request=None) -> str:
        '''
           authorization header function
        '''
        return None

    
