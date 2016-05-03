import unittest

class MongoDBBaseTest(unittest.TestCase):
   def setUp(self):
	self.connection=connect_to_mongodb()

class MySQLBaseTest(unittest.TestCase):
   def setUp(self):
	self.connection=connect_to_mysql()

class TestDatabase(unittest.TestCase):

