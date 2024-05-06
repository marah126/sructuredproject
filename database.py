from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from sqlalchemy.ext.declarative import declarative_base

user = 'root'
password = 'Marah@2001'
host = 'localhost'
port = 3307
database = 'test'

def get_connection():
    password_encoded = quote_plus(password)
    return create_engine(
        f"mysql+pymysql://{user}:{password_encoded}@{host}:{port}/{database}"
    )

engine = get_connection()
Session = sessionmaker(bind=engine)

Base = declarative_base()
