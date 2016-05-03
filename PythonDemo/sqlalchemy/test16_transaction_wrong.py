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
    money = Column(DECIMAL(10, 2))

class TanseferLog(BaseModel):
    __tablename__ = 'transfer_log'

    id = Column(Integer, primary_key=True)
    from_user = Column(Integer, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))
    to_user = Column(Integer, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))
    amount = Column(DECIMAL(10, 2))

# create tables automatically
BaseModel.metadata.create_all(engine)

user = User(money=100)
session.add(user)
user = User(money=0)
session.add(user)
session.commit()

session1 = DBSession()
session2 = DBSession()

user1 = session1.query(User).get(1)
user2 = session1.query(User).get(2)

if user1.money >= 100:
    user1.money -= 100
    user2.money += 100
    session1.add(TanseferLog(from_user=1, to_user=2, amount=100))

user1 = session2.query(User).get(1)
user2 = session2.query(User).get(2)
if user1.money >= 100:
    user1.money -= 100
    user2.money += 100
    session2.add(TanseferLog(from_user=1, to_user=2, amount=100))

session1.commit()
session2.commit()
session.close()

# 最终的结果是转账2次，每次转100元
# 1. 竟然能成功
# 2. transfer_log中有2条记录，与user中money对不上