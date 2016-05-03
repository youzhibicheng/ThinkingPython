from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine
from sqlalchemy.types import CHAR, Integer, String
from random import randint
from sqlalchemy import ForeignKey
from sqlalchemy import distinct
from sqlalchemy.orm import aliased

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

for i in xrange(10):
    session.add(User(age=randint(1, 10)))
# or session.commit()
session.flush()

for i in xrange(10):
    session.add(Friendship(user_id1=randint(1, 10), user_id2=randint(1, 10)))

session.commit()

Friend = aliased(User, name='Friend')

# select user.id from user, friendship where user.id=friendship.user_id1;
print session.query(User.id).join(Friendship, User.id == Friendship.user_id1).all()

# select distinct(user.id) from user, friendship where user.id=friendship.user_id1;
print session.query(distinct(User.id)).join(Friendship, User.id == Friendship.user_id1).all()
# the same as above
print session.query(User.id).join(Friendship, User.id == Friendship.user_id1).distinct().all()

# select distinct(friendship.user_id2) from friendship, user where user.id=friendship.user_id1 order by friendship.user_id2;
print session.query(Friendship.user_id2).join(User, User.id == Friendship.user_id1).order_by(Friendship.user_id2).distinct().all()
# the same as above, strange about select_from(User)???
print session.query(Friendship.user_id2).select_from(User).join(Friendship, User.id == Friendship.user_id1).order_by(Friendship.user_id2).distinct().all()

# select user.id, friendship.user_id2 from user, friendship where user.id=friendship.user_id1;
# if change to the following, are they the same ???
# session.query(User.id, Friendship.user_id2).join(User, User.id == Friendship.user_id1).all()
# will throw error
# *** InvalidRequestError: Can't join table/selectable 'user' to itself
# but this one is OK
# session.query(Friendship.user_id2, User.id).join(User, User.id == Friendship.user_id1).all()
print session.query(User.id, Friendship.user_id2).join(Friendship, User.id == Friendship.user_id1).all()
# select user.id, friendship.user_id2 from user, friendship where user.id=friendship.user_id1 and user.id < 10;
print session.query(User.id, Friendship.user_id2).join(Friendship, User.id == Friendship.user_id1).filter(User.id < 10).all()

# two join using the same table User, so need alias
# select user.id, friend.id from user, user as friend, friendship where user.id=friendship.user_id1 and friend.id=friendship.user_id2;
# this one is very difficult !!!!!!
# the same as
# select user_id1, user_id2 from friendship;
# translate is ""
print session.query(User.id, Friend.id).join(Friendship, User.id == Friendship.user_id1).join(Friend, Friend.id == Friendship.user_id2).all()
# select user.id, friendship.user_id2 from user left join friendship on user.id=friendship.user_id1;
# outerjoin -> left join, the result based on left side User
print session.query(User.id, Friendship.user_id2).outerjoin(Friendship, User.id == Friendship.user_id1).all()

session.close()
