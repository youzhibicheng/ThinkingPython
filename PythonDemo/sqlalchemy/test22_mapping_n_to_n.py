#coding=utf-8

from random import randint

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relation
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from sqlalchemy.orm import mapper
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

# If you want to use many-to-many relationships you will need to define a helper table that is used for the relationship.
# For this helper table it is strongly recommended to not use a model but an actual table:
# Many-to-many relationship 只需要在一边定义
# 一定要包含BaseModel.metadata,否则报错
# AttributeError: Neither 'Column' object nor 'Comparator' object has an attribute 'schema'
page_tag_table = Table('page_tag', BaseModel.metadata,
                       Column('page_id', Integer, ForeignKey('page.id')),
                       Column('tag_id', Integer, ForeignKey('tag.id')))


class Page(BaseModel):
    __tablename__ = 'page'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    tags = relationship('Tag', secondary=page_tag_table, backref=backref('pages', lazy='dynamic'))


class Tag(BaseModel):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    # pages = relationship('Page', secondary=page_tag_table, backref=backref('tags', lazy='dynamic'))

# mapper(Page, page_table, properties={'tags': relation(Tag, secondary=page_tag_table, backref='pages')})
# mapper(Tag, tag_table)

# create tables automatically
BaseModel.metadata.create_all(engine)

page1 = Page(name='page1')
session.add(page1)
tag1 = Tag(name='tag1')
session.add(tag1)
tag2 = Tag(name='tag2')
session.add(tag2)
page1.tags.append(tag1)
page1.tags.append(tag2)

tag3 = Tag(name='tag3')
session.add(tag3)
page2 = Page(name='page2')
session.add(page2)
page3 = Page(name='page3')
session.add(page3)
tag3.pages.append(page2)
tag3.pages.append(page3)
session.commit()
session.close()
