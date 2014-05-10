from db import LogifyDB

class Logify(object):
	"""docstring for ClassName"""
	def __init__(self, projectname):
		self.projectname = projectname
		self.dbhandler = LogifyDB(dbtype='sqlite',dbname=projectname)

	def log (self , type, message):
		result=self.dbhandler.commit(type=type,message=message)
		return result

	def readerrors(self,type):
		result=self.dbhandler.getlogfromtype(type=type)
		return result