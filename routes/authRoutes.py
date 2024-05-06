# routes/authRoutes.py

from flask import Blueprint, jsonify, request
from flask_bcrypt import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
from database import Session
from models.auth import Auth
import re

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=["POST"])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    confirm = data.get('confirm')

    if len(username) < 5:
        return jsonify({'error': 'Username should be at least 5 characters long'}), 400

    if password != confirm:
        return jsonify({'error': 'Password and confirmation do not match'}), 400

    if len(password) < 8 or not re.search("[a-z]", password) or not re.search("[A-Z]", password) or not re.search("[0-9]", password) or not re.search("[!@#$%^&*()_+=]", password):
        return jsonify({'error': 'Password is not strong. It should be at least 8 characters and contain lowercase, uppercase, numeric, and special characters'}), 400

    session = Session()
    existing_user = session.query(Auth).filter_by(username=username).first()
    if existing_user:
        session.close()
        return jsonify({'error': 'Username already exists. Choose another one'}), 400

    hashed_password = generate_password_hash(password).decode('utf-8')
    user = Auth(username=username, password=hashed_password)
    session.add(user)
    session.commit()
    session.close()

    return jsonify({'message': 'Success! Welcome to our system, ' + username + '!'}), 200


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    session = Session()
    user = session.query(Auth).filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        session.close()
        return jsonify({'message': 'Welcome back, ' + username + '!'}), 200
    else:
        session.close()
        return jsonify({'error': 'Invalid username or password'}), 401
