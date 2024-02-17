#!/usr/bin/env python3
'''
   Session_auth module
'''
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    '''SessionAuth class
    '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''
           Creating a session id for a user
        '''
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id.update(
                {id: user_id})
        return id
