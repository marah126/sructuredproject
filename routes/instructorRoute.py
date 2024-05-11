from flask import Blueprint, jsonify, request
from database import Session
from models.instructor import Instructor
import loggingg
from errors import internal_server_error, UsernameAlreadyExistsError, ResourceNotFoundError
instructor_bp = Blueprint('instructor', __name__)

# API to get all instructors
@instructor_bp.route('/instructors', methods=['GET'])
def get_instructors():
    try:
        session = Session()
        instructors = session.query(Instructor).all()
        session.close()
        return jsonify([{
            'id': instructor.id,
            'name': instructor.name,
            'email': instructor.emaill,
            'department': instructor.department
        } for instructor in instructors])
    except Exception as e:
        loggingg.errorLogger.exception("An error occurred while retrieving instructors: %s \n", e)
        raise internal_server_error(f'{e} error occurred while retrieving instructors')


# API to create a new instructor
@instructor_bp.route('/newInstructor', methods=['POST'])
def create_instructor():
    try:
        data = request.json
        id = data.get('id')
        name = data.get('name')
        email = data.get('email')
        department = data.get('department')

        if not id or not name or not email or not department:
            return jsonify({'error': 'Incomplete data '}), 400

        new_instructor = Instructor(id=id, name=name, email=email, department=department)

        session = Session()
        session.add(new_instructor)
        session.commit()
        session.close()

        return jsonify({'message': 'Instructor added successfully'}), 200
    except Exception as e:
        loggingg.errorLogger.exception("An error occurred while creating the instructor: %s", e)
        raise internal_server_error(f'{e} error occurred while creating the instructor')
