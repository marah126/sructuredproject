from flask import Flask, jsonify
from routes import authRoutes, studentRoute, instructorRoute, courseRoutes
from database import Session, Base
from errors import not_found_error,internal_server_error
app = Flask(__name__)


app.register_blueprint(authRoutes.auth_bp)
app.register_blueprint(studentRoute.student_bp)
app.register_blueprint(instructorRoute.instructor_bp)
app.register_blueprint(courseRoutes.course_bp)

app.config["SECRET_KEY"] = "MarahD"

# Base.metadata.create_all()
app.register_error_handler(404, not_found_error)
app.register_error_handler(500, internal_server_error)
if __name__ == '__main__':from flask import Flask, jsonify
from routes import authRoutes, studentRoute, instructorRoute, courseRoutes
from database import Session, Base
from errors import not_found_error, internal_server_error

app = Flask(__name__)

app.register_blueprint(authRoutes.auth_bp)
app.register_blueprint(studentRoute.student_bp)
app.register_blueprint(instructorRoute.instructor_bp)
app.register_blueprint(courseRoutes.course_bp)

app.config["SECRET_KEY"] = "MarahD"

# Base.metadata.create_all()
app.register_error_handler(404, not_found_error)
app.register_error_handler(500, internal_server_error)

if __name__ == '__main__':
    try:
        print("Server started successfully.")
        app.run(debug=True)
    except Exception as ex:
        print("Server could not be started due to the following error:\n", ex)

    try:
        print("Server started successfully.")
        app.run(debug=True)
    except Exception as ex:
        print("Server could not be started due to the following error:\n", ex)
