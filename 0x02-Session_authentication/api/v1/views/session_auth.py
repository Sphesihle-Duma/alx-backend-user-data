#!/usr/bin/env python3
'''
   session view module
'''
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    '''
       Post request for login
       return logged in user
    '''
    email = request.form.get('email')
    if not email:
        return jsonify({'error': 'email missing'}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({'error': 'password missing'}), 400
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({'error': 'no user found for this email'}), 404
    if not users:
        return jsonify({'error': 'no user found for this email'}), 404
    for user in users:
        if not user.is_valid_password(password):
            return jsonify({'error': 'wrong password'}), 401

    from api.v1.app import auth
    logged_in_user = users[0]
    session_id = auth.create_session(user.id)

    SESSION_NAME = getenv('SESSION_NAME')
    response = jsonify(user.to_json())
    response.set_cookie(SESSION_NAME, session_id)

    return response

    @app_views.route('/auth_session/logout',
                     methods=['DELETE'], strict_slashes=False)
    def logout():
        ''' deleting a session
        '''
        from api.vi.app import auth
        if not auth.destroy_session(request):
            print('Entering the 404')
            abort(404)
        return jsonify({}), 200
