#coding=utf-8

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine
from sqlalchemy.types import Integer, String
from random import randint
from sqlalchemy import func, or_, not_

class ModelMixin(object):
    @classmethod
    def get_by_id(cls, session, id, columns=None, lock_mode=None):
        if hasattr(cls, 'id'):
            scalar = False
            if columns:
                if isinstance(columns, (tuple, list)):
                    query = session.query(*columns)
                else:
                    scalar = True
                    query = session.query(columns)
            else:
                query = session.query(cls)
            if lock_mode:
                query = query.with_lockmode(lock_mode)
            query = query.filter(cls.id == id)
            if scalar:
                return query.scalar()
            return query.first()
        return None

    @classmethod
    def get_all(cls, session, columns=None, offset=None, limit=None, order_by=None, lock_mode=None):
        if columns:
            if isinstance(columns, (tuple, list)):
                query = session.query(*columns)
            else:
                query = session.query(columns)
                if isinstance(columns, str):
                    query = query.select_from(cls)
        else:
            query = session.query(cls)
        if order_by is not None:
            if isinstance(order_by, (tuple, list)):
                query = query.order_by(*order_by)
            else:
                query = query.order_by(order_by)
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)
        if lock_mode:
            query = query.with_lockmode(lock_mode)
        return query.all()

    @classmethod
    def count_all(cls, session, lock_mode=None):
        query = session.query(func.count('*')).select_from(cls)
        if lock_mode:
            query = query.with_lockmode(lock_mode)
        return query.scalar()

    @classmethod
    def exist(cls, session, id, lock_mode=None):
        if hasattr(cls, 'id'):
            query = session.query(func.count('*')).select_from(cls).filter(cls.id == id)
            if lock_mode:
                query = query.with_lockmode(lock_mode)
            return query.scalar() > 0
        return False

    @classmethod
    def set_attr(cls, session, id, attr, value):
        if hasattr(cls, 'id'):
            session.query(cls).filter(cls.id == id).update({
                attr: value
            })
            session.commit()

    @classmethod
    def set_attrs(cls, session, id, attrs):
        if hasattr(cls, 'id'):
            session.query(cls).filter(cls.id == id).update(attrs)
            session.commit()

BaseModel = declarative_base(cls=ModelMixin)
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
    name = Column(String(30))

# create tables automatically
BaseModel.metadata.create_all(engine)

for i in xrange(10):
    session.add(User(age=randint(1, 10), name='Grace'))
session.commit()

test1 = User.get_by_id(session, 1)
print test1.age
# test2 is a list
test2 = User.get_all(session)
print test2[1].age
# test3 is a number
test3 = User.count_all(session)
print test3
# test4 is a boolean
test4 = User.exist(session, 2)
print test4
# update user set age=100 where id=1
test5 = User.set_attr(session, 1, "age", 100)
test_attrs = {'age' : 101, 'name': 'James'}
test6 = User.set_attrs(session, 2, test_attrs)

session.close()
