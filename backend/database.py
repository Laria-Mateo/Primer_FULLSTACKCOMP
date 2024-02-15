#Simport os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
#from dotenv import load_dotenv

#load_dotenv()

#DB_NAME = os.getenv('DB_NAME')
#DB_HOST = os.getenv('DB_HOST')
#DB_DIALECT = os.getenv('DB_DIALECT')
#DB_PASSWORD = os.getenv('DB_PASSWORD')
#DB_USER = os.getenv('DB_USER')

#SQLALCHEMY_DATABASE_URL = '{}://{}:{}@{}/{}'.format(DB_DIALECT, DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:12345@localhost:5433/MiBaseLocal"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

localSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

