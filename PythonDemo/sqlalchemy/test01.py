from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# the same as the following sql statement
# CREATE TABLE user(
#     id varchar(20),
#     name varchar(50),
#     PRIMARY KEY (id)
# );
class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(50))

class School(Base):
    __tablename__ = 'school'
    id = Column(String(20), primary_key=True)
    name = Column(String(50))

engine = create_engine('mysql://root:passw0rd@localhost:3306/sqlalchemy')
DBSession = sessionmaker(bind=engine)
session = DBSession()

# need to create table user in mysql DB first
new_user = User(id='1', name='JamesZOU')
session.add(new_user)

session.execute('use sqlalchemy')
print session.execute('select * from user where id = 1').first()
print session.execute('select * from user where id = :id', {'id': 1}).first()

session.execute('create database sqlalchemy2')
print session.execute('show databases').fetchall()

session.commit()
session.close()
