from sqlalchemy import func, or_, not_
from sqlalchemy import Column, create_engine
from sqlalchemy.types import CHAR, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BaseModel = declarative_base()
# need to create database sqlalchemy first
# mysql> create database sqlalchemy
# mysql> use sqlalchemy
engine = create_engine('mysql://root:passw0rd@localhost:3306/sqlalchemy')
DBSession = sessionmaker(bind=engine)
session = DBSession()
# this command will create tables automatically
BaseModel.metadata.create_all(engine)

class User(BaseModel):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(CHAR(30))

user = User(name='a')
session.add(user)
user = User(name='b')
session.add(user)
user = User(name='a')
session.add(user)
user = User()
session.add(user)
session.commit()

query = session.query(User)
print query
print query.statement
for user in query:
    print user.name
print query.all()
# first() will return None if result is empty
print query.first().name
# one() will throw exception if result is empty or multi lines
#print query.one().name
print query.filter(User.id == 2).first().name
# get() using the primary key, the same as above
print query.get(2).name
print query.filter('id = 2').first().name

query2 = session.query(User.name)
print query2.all()
print query2.limit(1).all()
# begin from line 2
print query2.offset(1).all()
print query2.order_by(User.name).all()
print query2.order_by('name').all()
print query2.order_by(User.name.desc()).all()
print query2.order_by('name desc').all()
print session.query(User.id).order_by(User.name.desc(), User.id).all()

# return the 1st element in 1st line if result is not empty
# scalar() will invoke one(), will throw exception if return multiple values
print query2.filter(User.id == 1).scalar()
print session.query('id').select_from(User).filter('id = 1').scalar()
# if User.name is None, will filter
print query2.filter(User.id > 1, User.name != 'a').scalar()
query3 = query2.filter(User.id > 1)
query3 = query3.filter(User.name != 'a')
print query3.scalar()
# or_
print query2.filter(or_(User.id == 1, User.id == 2)).all()
# in_
print query2.filter(User.id.in_((1, 2))).all()

query4 = session.query(User.id)
print query4.filter(User.name == None).scalar()
print query4.filter('name is null').scalar()
# not_
print query4.filter(not_(User.name == None)).all()
print query4.filter(User.name != None).all()

print query4.count()
# the same as
# select count(*) from user
print session.query(func.count('*')).select_from(User).scalar()
# select count(1) from user
print session.query(func.count('1')).select_from(User).scalar()
# select count(id) from user
print session.query(func.count(User.id)).scalar()
# Because there is User.id, so do not need to identify table User
# select count(*) from user where id > 0
print session.query(func.count('*')).filter(User.id > 0).scalar()
# select count(*) from user where name='a'
print session.query(func.count('*')).filter(User.name == 'a').limit(1).scalar() == 1
# select sum(id) from user
print session.query(func.sum(User.id)).scalar()
# func can invoke any functions if the database support
# select now() from user
print session.query(func.now()).scalar()
# select current_timestamp() from user
print session.query(func.current_timestamp()).scalar()
# select md5(name) from user where id=1
print session.query(func.md5(User.name)).filter(User.id == 1).scalar()
# update user set name=c where id=1
query.filter(User.id == 1).update({User.name: 'c'})
user = query.get(1)
# the print value is c, not in database still a
print user.name

user.name = 'd'
# write, but do not commit
session.flush()
# the print value is d, but in database still a
print query.get(1).name
# do not delete in database
session.delete(user)
session.flush()
# the value is None, not a, but in database still a
print query.get(1)

session.rollback()
print query.get(1).name
query.filter(User.id == 1).delete()
# delete from user where id=1, deleted in database now
session.commit()
# the result is none
print query.get(1)
