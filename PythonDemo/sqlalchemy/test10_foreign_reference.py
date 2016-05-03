from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine
from sqlalchemy.types import CHAR, Integer, String
from random import randint
from sqlalchemy import ForeignKey

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


class Friendship(BaseModel):
    __tablename__ = 'friendship'

    id = Column(Integer, primary_key=True)
    user_id1 = Column(Integer, ForeignKey('user.id'))
    user_id2 = Column(Integer, ForeignKey('user.id'))
    #user_id1 = Column(Integer, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))
    #user_id2 = Column(Integer, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))
    
# create tables automatically
BaseModel.metadata.create_all(engine)

for i in xrange(100):
    session.add(User(age=randint(1, 100)))
# or session.commit()
session.flush()

for i in xrange(100):
    session.add(Friendship(user_id1=randint(1, 100), user_id2=randint(1, 100)))

session.commit()

# can not delete because table friendship reference to it
session.query(User).filter(User.age < 50).delete()

session.close()
