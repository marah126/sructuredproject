from flask import Flask
from routes import authRoutes, studentRoute, instructorRoute, courseRoutes
from database import Session, Base

app = Flask(__name__)

# Register blueprints
app.register_blueprint(authRoutes.auth_bp)
app.register_blueprint(studentRoute.student_bp)
app.register_blueprint(instructorRoute.instructor_bp)
app.register_blueprint(courseRoutes.course_bp)

# Set secret key
app.config["SECRET_KEY"] = "MarahD"

# Create database tables
# Base.metadata.create_all()

if __name__ == '__main__':
    try:
        print("Server started successfully.")
        app.run(debug=True)
    except Exception as ex:
        print("Server could not be started due to the following error:\n", ex)
