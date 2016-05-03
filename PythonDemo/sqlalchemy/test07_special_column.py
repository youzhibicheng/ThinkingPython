from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine
from sqlalchemy.types import String
from sqlalchemy.types import CHAR

BaseModel = declarative_base()
# need to create database first
# mysql> create database sqlalchemy;
# mysql> use sqlalchemy;
engine = create_engine('mysql://root:passw0rd@localhost:3306/sqlalchemy')
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Test7(BaseModel):
    __tablename__ = 'test7'
    # using sql dialet
    from sqlalchemy.dialects.mysql import INTEGER
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name = Column(String(30))
    age = Column(INTEGER(unsigned=True))
    # from is a keyword in python
    from_ = Column('from', CHAR(10))

# create tables automatically
BaseModel.metadata.create_all(engine)

new_user = Test7(name='test7', age=30)
session.add(new_user)
session.commit()

# how to get a column length
print Test7.name.property.columns[0].type.length

session.close()
