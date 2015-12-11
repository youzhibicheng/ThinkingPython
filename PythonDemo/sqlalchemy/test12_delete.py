#coding=utf-8

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine
from sqlalchemy.types import Integer
from random import randint
from sqlalchemy import ForeignKey
from sqlalchemy import func, or_, not_

BaseModel = declarative_base()
# need to create database first
# mysql> create database sqlalchemy;
# mysql> use sqlalchemy;
engine = create_engine('mysql://root:passw0rd@localhost:3306/sqlalchemy')
DBSession = sessionmaker(bind=engine)
session = DBSession()

# drop table user first if table user exist
class User(BaseModel):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    age = Column(Integer)

# create tables automatically
BaseModel.metadata.create_all(engine)

for i in xrange(10):
    session.add(User(age=randint(1, 10)))
session.commit()

session.query(User).filter(or_(User.id == 1, User.id == 2, User.id == 3)).delete()
session.commit()

# throw error
# sqlalchemy.exc.InvalidRequestError: Could not evaluate current criteria in Python.  Specify 'fetch' or False for the synchronize_session parameter.
# 删除记录时，默认会尝试删除 session 中符合条件的对象，而 in 操作估计还不支持，于是就出错了
#session.query(User).filter(User.id.in_((1, 2, 3))).delete()

# 解决办法就是删除时不进行同步，然后再让 session 里的所有实体都过期：
session.query(User).filter(User.id.in_((4, 5, 6))).delete(synchronize_session=False)
# or session.expire_all()
session.commit()

session.close()
