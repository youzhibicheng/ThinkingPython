#coding=utf-8

from random import randint

from sqlalchemy import Column
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer
from sqlalchemy.types import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import AbstractConcreteBase

BaseModel = declarative_base()
# need to create database first
# mysql> create database sqlalchemy;
# mysql> use sqlalchemy;
engine = create_engine('mysql://root:passw0rd@localhost:3306/sqlalchemy')
DBSession = sessionmaker(bind=engine)
# also can use the following statements
# Session=sessionmaker()
# Session.configure(bind=engine)
session = DBSession()


class Employee(AbstractConcreteBase, BaseModel):
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def test(self):
        print self.name


class Manager(Employee):
    __tablename__ = 'manager'
    manager_name = Column(String(40))
    __mapper_args__ = {
        'polymorphic_identity': 'manager',
        'concrete': True
    }


class Engineer(Employee):
    __tablename__ = 'engineer'
    engineer_name = Column(String(40))
    __mapper_args__ = {
        'polymorphic_identity': 'engineer',
        'concrete': True
    }

# create tables automatically
BaseModel.metadata.create_all(engine)

eng = Engineer(name="JamesZOU", engineer_name="Software Engineer")
session.add(eng)
man = Manager(name="GraceLi", manager_name="Manager")
session.add(man)
session.commit()
session.close()
