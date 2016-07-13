from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime, time

class User(Base):
	__tablename__ = 'user_table'
	user_id = Column(String(30), primary_key=True)
	user_name = Column(String(40))
	created = Column(DateTime)

	def __init__(self, user_id, name):
		self.user_id = user_id
		self.user_name = name
		self.created = datetime.datetime.now()

	def __repr__(self):
		return '{user_id : "%s", user_name : "%s", created : "%s"}' %\
				{self.user_id, self.user_name, self.created}









