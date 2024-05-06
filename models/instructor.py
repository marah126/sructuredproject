from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Instructor(Base):
    __tablename__ = 'instructors'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    department = Column(String(100))

    # Define the relationship after the Course class is defined
    courses = relationship("Course", back_populates="instructor")