#!/usr/bin/env python3
'''
   Session_auth module
'''
from api.v1.auth.auth import Auth
import uuid
from models.user import User


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

    def current_user(self, request=None):
        """Returns a User instance based on a cookie value"""

        session_id = self.session_cookie(request)

        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        print(f'the use id is {user_id}')
        if user_id is None:
            return None

        return User.get(user_id)

    def destroy_session(self, request=None):
        '''destroying a session
        '''
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id
        if user_id is None:
            return False
        try:
            del self.user_id_by_sessio_id[session_id]
        except Exception:
            pass
        return True
