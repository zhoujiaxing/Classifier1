import pymongo
from pymongo import MongoClient
class MongoCli(object):
	def __init__(self):
		self.client = MongoClient('localhost',27017)
	def getdata(self,database,collection):
		db = self.client[database]
		coll = db[collection]
		return coll
