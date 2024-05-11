
from flask import Blueprint, jsonify, request
from flask_bcrypt import generate_password_hash, check_password_hash
from database import Session
from models.auth import Auth
import re
import loggingg
from errors import internal_server_error, UsernameAlreadyExistsError, ResourceNotFoundError


auth_bp = Blueprint('auth', __name__)
print("hi")
@auth_bp.route('/signup', methods=["POST"])
def register():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        confirm = data.get('confirm')

        if len(username) < 5:
            raise ValueError('Username should be at least 5 characters long')

        if password != confirm:
            raise ValueError('Password and confirmation do not match')

        if len(password) < 8 or not re.search("[a-z]", password) or not re.search("[A-Z]", password) or not re.search("[0-9]", password) or not re.search("[!@#$%^&*()_+=]", password):
            raise Exception('Password is not strong. It should be at least 8 characters and contain lowercase, uppercase, numeric, and special characters')

        session = Session()
        existing_user = session.query(Auth).filter_by(username=username).first()
        if existing_user:
            session.close()
            raise UsernameAlreadyExistsError()

        hashed_password = generate_password_hash(password).decode('utf-8')
        user = Auth(username=username, password=hashed_password)
        session.add(user)
        session.commit()
        session.close()

        loggingg.signupLogger.info('New user registered: %s', username)

        return jsonify({'message': 'Success! Welcome to our system, ' + username + '!'}), 200
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except UsernameAlreadyExistsError as ue:
        return jsonify({'error': str(ue)}), 400
    except Exception as e:
        loggingg.errorLogger.exception("An error occurred: %s", e)
        raise internal_server_error(e)


@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        session = Session()
        user = session.query(Auth).filter_by(username=username).first()

        if not user:
            raise ResourceNotFoundError('User not found')

        if user and check_password_hash(user.password, password):
            session.close()
            loggingg.loginLogger.info("Logged in successfully: %s", username)
            return jsonify({'message': 'Welcome back, ' + username + '!'}), 200
        else:
            session.close()
            return jsonify({'error': 'Invalid username or password'}), 401

    except ResourceNotFoundError as re:
        return jsonify({'error': str(re)}), 404
    except Exception as e:
        loggingg.errorLogger.exception("An error occurred: %s", e)
        raise internal_server_error(e)

