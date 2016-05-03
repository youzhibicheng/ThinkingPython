from sqlalchemy import Column, create_engine
from sqlalchemy.types import CHAR, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BaseModel = declarative_base()
# need to create database sqlalchemy first
engine = create_engine('mysql://root:passw0rd@localhost:3306/sqlalchemy')
DBSession = sessionmaker(bind=engine)
session = DBSession()

# BaseModel.metadata.create_all(engine)
# will find all the classes that inherit from BaseModel and create related table in database
def init_db():
    BaseModel.metadata.create_all(engine)

def drop_db():
    BaseModel.metadata.drop_all(engine)

class User(BaseModel):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(CHAR(30))

class School(BaseModel):
    __tablename__ = 'school'
    id = Column(String(20), primary_key=True)
    name = Column(String(50))

init_db()
