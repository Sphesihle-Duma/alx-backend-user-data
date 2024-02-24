#!/usr/bin/env python3
'''
   A basic flask app
'''
from flask import Flask, jsonify, request, abort, redirect, url_for
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/')
def home():
    '''
        view function
    '''
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user():
    ''' Registering users
        the data will come from a form
        form data:
          email: user email
          password: user password
    '''
    email = request.form['email']
    password = request.form['password']
    if email and password:
        try:
            if AUTH.register_user(email, password):
                return jsonify({"email": email, "message": "user created"})
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST', 'DELETE'], strict_slashes=False)
def login():
    '''
      create a session for user
      with valid logins
    '''
    if method == 'DELETE':
        cookie_session_id = request.cookies.get('session_id')
        if cookie_session_id:
            user = AUTH.get_user_from_session_id(cookie_session_id)
            if user:
                AUTH.destroy_session(user.id)
                return redirect(url_for('home'))
            abort(403)

    email = request.form['email']
    password = request.form['password']
    if email and password:
        validated_user = AUTH.valid_login(
                email=email,
                password=password)
        if validated_user:
            session_id = AUTH.create_session(email)
            response = jsonify(
                    {'email': email, 'message': 'logged in'})
            response.set_cookie('session_id', session_id)
            return response, 200
    abort(401)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
