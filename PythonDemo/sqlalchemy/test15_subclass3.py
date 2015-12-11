#coding=utf-8

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine
from sqlalchemy.types import Integer, String
from random import randint

BaseModel = declarative_base()

# need to create database first
# mysql> create database sqlalchemy;
# mysql> use sqlalchemy;
engine = create_engine('mysql://root:passw0rd@localhost:3306/sqlalchemy')
DBSession = sessionmaker(bind=engine)
session = DBSession()


# use __abstract__ = True to define
class AbstractUser(BaseModel):
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    __abstract__ = True
    # 可以省掉子类的 __table_args__ 了
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }


class User(AbstractUser):
    __tablename__ = 'user'

    name = Column(String(30))

class Student(AbstractUser):
    __tablename__ = 'student'

    teacher = Column(String(30))


# create tables automatically
BaseModel.metadata.create_all(engine)

for i in xrange(10):
    session.add(User(age=randint(1, 10), name='randint(1, 100)'))
for i in xrange(10):
    session.add(Student(age=randint(1, 10), teacher='teacher'))
session.commit()

session.close()
