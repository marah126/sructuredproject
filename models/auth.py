from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Auth(Base):
    __tablename__ = 'auth'
    id = Column(Integer, primary_key=True, autoincrement=True)  # Make id auto-incrementing
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

