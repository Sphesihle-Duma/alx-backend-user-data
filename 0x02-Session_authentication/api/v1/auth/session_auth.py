#!/usr/bin/env python3
'''
   Session_auth module
'''
from api.v1.auth.auth import Auth
import uuid
import os


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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''
        Returning user id based on a session id
        '''
        if session_id is None:
            return None

        if not isinstance(session_id, str):
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)
