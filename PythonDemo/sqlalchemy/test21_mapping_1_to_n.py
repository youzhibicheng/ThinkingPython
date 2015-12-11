#coding=utf-8

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
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

# 父亲和孩子是1对n的关系
class Father(BaseModel):
    __tablename__ = 'father'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    children = relationship('Child', backref='father', lazy='dynamic')

class Child(BaseModel):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    father_id = Column(Integer, ForeignKey('father.id'))

# create tables automatically
BaseModel.metadata.create_all(engine)

father = Father(name='James ZOU')
session.add(father)
child = Child(name='Mints ZOU')
session.add(child)
father.children = [child]
session.commit()

father2 = Father(name='William')
session.add(father2)
# must need commit first, 否则接下来的father2.id是None
session.commit()
child2 = Child(name='Charles')
child2.father_id = father2.id
session.add(child2)
session.commit()

father = session.query(Father).filter(Father.id == 1).all()
print father[0].id
print father[0].name
children = father[0].children
print children[0].id
print children[0].name

session.close()
