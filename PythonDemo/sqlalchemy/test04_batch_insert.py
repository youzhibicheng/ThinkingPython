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
# this command will create tables automatically
BaseModel.metadata.create_all(engine)

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


session.execute(
    User.__table__.insert(),
    [{'name': 'randint(1, 100)', 'age': randint(1, 100)} for i in xrange(10000)]
)
session.commit()
