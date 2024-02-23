#!/usr/bin/env python3
'''
   A basic flask app
'''
from flask import Flask, jsonify, request
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')