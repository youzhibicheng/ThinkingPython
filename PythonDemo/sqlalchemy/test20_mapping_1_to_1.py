#coding=utf-8

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
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


# 父亲和孩子是1对1的关系
class Father(BaseModel):
    __tablename__ = 'father'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    child_id = Column(Integer, ForeignKey('child.id'))
    # child = relationship('Father', backref='child', lazy='dynamic', uselist=False)\
    child = relationship('Child', backref=backref('father', order_by=id))


class Child(BaseModel):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))

# create tables automatically
BaseModel.metadata.create_all(engine)

father = Father(name='James ZOU')
session.add(father)
son = Child(name='Mints ZOU')
session.add(son)
father.child = son
session.commit()

session.close()
