#coding=utf-8

from random import randint
import sqlalchemy
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapper
from sqlalchemy.types import Integer
from sqlalchemy.types import DECIMAL
from sqlalchemy.types import String
from sqlalchemy.ext.declarative import declarative_base

print sqlalchemy.__version__
# 定义引擎
engine = create_engine('sqlite:///./sqlalchemy.db', echo=True)
# 绑定元信息
metadata = MetaData(engine)
user_table = Table('user', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String),
                   Column('fullname', String),
                   Column('password', String)
                   )
user_table.create()
# if not use metadata = MetaData(engine), please use the following
# metadata.create_all(engine)


class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.name, self.fullname, self.password)

mapper(User, user_table)

ed_user = User('ed', 'Ed Jones', 'edspassword')
print ed_user.name
print ed_user.password
# class User do not have id
print ed_user.id
