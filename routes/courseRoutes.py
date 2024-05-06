from flask import Blueprint, jsonify, request
from models.course import Course
from models.instructor import Instructor

from database import Session

course_bp = Blueprint('course', __name__)


# API to get all courses
@course_bp.route('/courses', methods=['GET'])
def get_courses():
    session = Session()
    courses = session.query(Course).all()
    session.close()
    return jsonify([{
        'id': course.id,
        'name': course.name,
        'instructor_id': course.instructor_id,
        'credits': course.credits
    } for course in courses])





# API to create a new course
@course_bp.route('/newCourse', methods=['POST'])
def create_course():
    data = request.json
    id = data.get('id')
    name = data.get('name')
    instructor_id = data.get('instructor_id')
    credits = data.get('credits')
    session = Session()

    if not id or not name or not instructor_id or not credits:
        return jsonify({'error': 'Incomplete data '}), 400

    instructor = session.query(Instructor).filter_by(id=instructor_id).first()
    if not instructor:
        return jsonify({'error': 'Instructor with ID {} not found'.format(instructor_id)}), 404

    new_course = Course(id=id, name=name, instructor_id=instructor_id, credits=credits)

    # Add the new course to the database
    session.add(new_course)
    session.commit()

    return jsonify({'message': 'Course added successfully'}), 200



# API to get all courses of an instructor by name
@course_bp.route('/coursesByInstructor', methods=['GET'])
def get_courses_instructor():
    data = request.json
    instructor_name = data.get('name')
    session = Session()
    if not instructor_name:
        return jsonify({'error': 'enter instructor name'}), 400

    instructor = session.query(Instructor).filter_by(name=instructor_name).first()

    if not instructor:
        return jsonify({'error': 'Instructor not exist'}), 404

    # Get all courses taught by the instructor
    courses = session.query(Course).filter_by(instructor_id=instructor.id).all()

    # Prepare the response data
    courses_data = [{'id': course.id, 'name': course.name, 'credits': course.credits} for course in courses]

    return jsonify(courses_data), 200
