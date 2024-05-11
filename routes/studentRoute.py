from flask import Blueprint, jsonify, request
from models.student import Student
from database import Session
import loggingg
from errors import internal_server_error, UsernameAlreadyExistsError, ResourceNotFoundError
student_bp = Blueprint('student', __name__)

# API to get all students
@student_bp.route('/students', methods=['GET'])
def get_students():
    try:
        session = Session()
        students = session.query(Student).all()
        session.close()
        return jsonify([{'id': student.id, 'name': student.name, 'age': student.age, 'email': student.email} for student in students])
    except Exception as e:
        loggingg.errorLogger.exception("An error occurred while retrieving students: %s", e)
        raise internal_server_error(f'{e} error occurred while retrieving students')


# API to create a new student
@student_bp.route('/newStudent', methods=['POST'])
def create_student():
    try:
        data = request.json
        id = data.get('id')
        name = data.get('name')
        age = data.get('age')
        email = data.get('email')

        if not id or not name or not age or not email:
            return jsonify({'error': 'Incomplete data'}), 400

        new_student = Student(id=id, name=name, age=age, email=email)

        session = Session()
        session.add(new_student)
        session.commit()
        session.close()

        return jsonify({'message': 'New student added successfully'}), 200
    except Exception as e:
        loggingg.errorLogger.exception("An error occurred while creating a new student: %s", e)
        raise internal_server_error(f'{e} error occurred while creating a new student')


# API to delete a student by ID
@student_bp.route('/deleteStudent/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        session = Session()
        student = session.query(Student).filter_by(id=student_id).first()

        if not student:
            return jsonify({'error': 'Student not found'}), 404

        # Delete the student from the database
        session.delete(student)
        session.commit()

        return jsonify({'message': 'Student deleted successfully'}), 200
    except Exception as e:
        loggingg.errorLogger.exception("An error occurred while deleting the student: %s", e)
        raise internal_server_error(f'{e} error occurred while deleting the student')

# API to update student email by ID
@student_bp.route('/updateEmail', methods=['PUT'])
def update_student_email():
    try:
        session = Session()
        data = request.json
        student_id = data.get('id')
        email = data.get('newEmail')
        student = session.query(Student).filter_by(id=student_id).first()

        if not student:
            return jsonify({'error': 'Student not found'}), 404

        if not email:
            return jsonify({'error': 'Email not provided in the body'}), 400

        student.email = email

        session.commit()

        return jsonify({'message': 'Student email updated successfully'}), 200
    except Exception as e:
        loggingg.errorLogger.exception("An error occurred while updating student email: %s", e)
        raise internal_server_error(f'{e} error occurred while updating student email')