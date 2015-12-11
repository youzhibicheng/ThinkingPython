from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine
from sqlalchemy.types import CHAR, Integer, String
from random import randint

BaseModel = declarative_base()
# need to create database first
# mysql> create database sqlalchemy;
# mysql> use sqlalchemy;
engine = create_engine('mysql://root:passw0rd@localhost:3306/sqlalchemy')
DBSession = sessionmaker(bind=engine)
session = DBSession()

# CREATE TABLE `user` (
# `id`  integer NULL AUTO_INCREMENT ,
# `name`  varchar(30) NULL ,
# `age`  integer NULL DEFAULT NULL ,
# PRIMARY KEY (`id`)
# );
class User(BaseModel):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    age = Column(Integer)

# create tables automatically
BaseModel.metadata.create_all(engine)

new_user = User(name='test5', age=30)
session.add(new_user)
session.commit()

# do not understand what is "prefix"
# is a MySQL statement
prefixes1 = session.query(User.name).prefix_with('HIGH_PRIORITY').all()
print prefixes1
prefixes2 = session.execute(User.__table__.insert().prefix_with('IGNORE'), {'id': 1, 'name': '1'})
print prefixes2

session.close()
