import pymongo
class CreatData(object):
	def __init__(self,collection=None):
		self.collection = collection
	'''
	parameter:
		num need text number
		category need text category
		refuse refuse text categorys
	return if number enough return corpus
			else reutrn None
	'''
	def setcollection(self,collection):
		self.collection = collection

	def getTextData(self,num,category,refuse=None):#
                datas = self.collection.find()
                corpus = []
                count = 0
                for data in datas:
			#print data
			try:
                       		categorys = data['category']
                      		if category == categorys:
                                	text = data['article']
                               		corpus.append(text)
                                	count = count + 1
			except:
				#print "Fiald in %d...."%count
				category
                        if count == num:
                                break
                if count == num:
                        return corpus
                else:
			print count,category
                        return corpus

	'''
	def getTextDatas(self,num,category,refuse):#
		datas = self.collection.find()
		corpus = []
		count = 0
		for data in datas:
			categorys = data['category']
			if (category in categorys) and (refuse not in categorys) :
				text = data['text']
				corpus.append(text)
				count = count + 1
			if count == num:
				break
		if count == num:
			return corpus
		else:
			return None
	'''
