#coding=utf-8

from random import randint

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer
from sqlalchemy.types import DECIMAL
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()
# need to create database first
# mysql> create database sqlalchemy;
# mysql> use sqlalchemy;
engine = create_engine('mysql://root:passw0rd@localhost:3306/sqlalchemy')
DBSession = sessionmaker(bind=engine)
session = DBSession()


class User(BaseModel):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    age = Column(Integer)

# create tables automatically
BaseModel.metadata.create_all(engine)

user = User(age=100)
session.add(user)
user = User(age=1)
session.add(user)
session.commit()

user = session.query(User).with_lockmode('update').get(1)
user.age += 1
session.commit()

session.query(User).filter(User.id == 1).update({
    User.age: User.age + 1
})
session.commit()

# 其实字段之间也可以做运算
session.query(User).filter(User.id == 1).update({
    User.age: User.age + User.id
})
session.commit()

session.close()