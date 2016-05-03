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

user1 = session1.query(User).with_lockmode('read').get(1)
user2 = session1.query(User).with_lockmode('read').get(2)
# user1 = session1.query(User).with_lockmode('update').get(1)
# user2 = session1.query(User).with_lockmode('update').get(2)
if user1.money >= 100:
    user1.money -= 100
    user2.money += 100
    session1.add(TanseferLog(from_user=1, to_user=2, amount=100))

# user1 = session2.query(User).with_lockmode('read').get(1)
# user2 = session2.query(User).with_lockmode('read').get(2)
user1 = session2.query(User).with_lockmode('update').get(1)
user2 = session2.query(User).with_lockmode('update').get(2)
if user1.money >= 100:
    user1.money -= 100
    user2.money += 100
    session2.add(TanseferLog(from_user=1, to_user=2, amount=100))

# 如果使用read锁,因为 user1 和 user2 都被 session2 加了读锁，所以会等待锁被释放
# session1.commit的时候就会锁死
# 超时以后，session1.commit() 会抛出个超时的异常，如果捕捉了的话，或者 session2 在另一个进程，那么 session2.commit() 还是能正常提交的。
# 这种情况下,有一个事务是肯定会提交失败的，所以那些更改等于白做了
session1.commit()
session2.commit()
session.close()

# 如果需要更改数据，最好加写锁。
# 如果要保证事务运行期间内，被读取的数据不被修改，自己也不去修改，加读锁即可。

# 这个实例没有完成，需要自己再测试