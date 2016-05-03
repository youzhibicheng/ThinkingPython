from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine
from sqlalchemy.types import CHAR, Integer, String

BaseModel = declarative_base()
# need to create database first
# mysql> create database sqlalchemy;
# mysql> use sqlalchemy;
engine = create_engine('mysql://root:passw0rd@localhost:3306/sqlalchemy')
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Test9(BaseModel):
    __tablename__ = 'test9'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    age = Column(Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "<User('%s')>" % (self.name,)

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
    }

# create tables automatically
BaseModel.metadata.create_all(engine)

# how to get a column length
print Test9.name.property.columns[0].type.length

session.close()
