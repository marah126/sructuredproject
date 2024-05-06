from flask import Blueprint, jsonify, request
from database import Session
from models.instructor import Instructor
instructor_bp = Blueprint('instructor', __name__)


#API to get all instructors
@instructor_bp.route('/instructors', methods=['GET'])
def get_instructors():
    session = Session()
    instructors = session.query(Instructor).all()
    session.close()
    return jsonify([{
        'id': instructor.id,
        'name': instructor.name,
        'email': instructor.email,
        'department': instructor.department
    } for instructor in instructors])




# API to create a new instructor
@instructor_bp.route('/newInstructor', methods=['POST'])
def create_instructor():
    data = request.json
    id=data.get('id')
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

