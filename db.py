import dataset
from datetime import datetime


class LogifyDB(object):

	"""docstring for ClassName"""

	def __init__(self, dbtype='sqlite', dbname="logs"):
		self.dbtype = dbtype
		self.dbname = dbname + ".db"
		self.db = dataset.connect('sqlite:///%s' % (self.dbname))
		if self.dbname == "sqlite":
			self.db = dataset.connect('sqlite:///%s' % (self.dbname))

		self.table = self.db['logs']

	def commit(self, type, message):
		cmt = self.table.insert(
			dict(type=type, message=message, timestamp=datetime.now()))
		return cmt

	def getlogs(self):
		for log in self.table:
   			yield log

   	def getlogfromtype(self,type):
   		logs_type = self.table.find(type=type)
   		return logs_type
