#coding=utf-8

from random import randint

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer
from sqlalchemy.types import String
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()
# need to create database first
# mysql> create database sqlalchemy;
# mysql> use sqlalchemy;
engine = create_engine('mysql://root:passw0rd@localhost:3306/sqlalchemy')
DBSession = sessionmaker(bind=engine)
session = DBSession()


class Employee(BaseModel):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    type = Column(String(20))
    engineer_name = Column(String(50))
    manager_name = Column(String(50))

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'employee'
   }


class Manager(Employee):
    __mapper_args__ = {
        'polymorphic_identity': 'manager'
    }


class Engineer(Employee):
    __mapper_args__ = {
        'polymorphic_identity': 'engineer'
    }

# create tables automatically
BaseModel.metadata.create_all(engine)

emp = Employee(name='Allen')
session.add(emp)
eng = Engineer(name="JamesZOU", engineer_name="Software Engineer")
session.add(eng)
man = Manager(name="GraceLi", manager_name="Manager")
session.add(man)
session.commit()
session.close()
