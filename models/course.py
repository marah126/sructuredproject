from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    instructor_id = Column(Integer, ForeignKey('instructors.id'))
    credits = Column(Integer)

    # Define the relationship after the Instructor class is defined
    instructor = relationship("Instructor", back_populates="courses")

