from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from pymongo import MongoClient
import pymongo
import creatdata
import classifier
import mongocli


cates=["Auto","Business","Cricket","Entertainment/Bollywood","Health","Lifestyle","National","Politics","Sports","Technology","World"]


class ModelClass(object):
	def __init__(self,category="Sports"):
		self.getdata = creatdata.CreatData(category)
		self.classifier = classifier.Classifier()
		self.getdata.setcollection(mongocli.MongoCli().getdata("mydb","web"))
		self.dirctory = {}
		self.category = category
	def train(self,t_num,x_num):
		words = self.dirctory.keys()
		corpus = []
		#train vectorizer
		for word in words:
			texts = self.dirctory[word]
			corpus.extend(texts[0,t_num])
		self.calssifier.trainvectorizer(corpus)
		#train classifier
		train_x = []
		train_y = []
		text_p = []
		text_n = []
		for word in words:
			texts = self.dirctory[word]
			if word == self.category:
				text_p.extend(texts[0,x_num*10])
			else:
				text_n.entend(texts[0,num])
		for text in text_p:
			train_x.append(self.classifier.getfeature(text))
			train_y.append(1)
		for text in text_n:
			train_x.append(self.classifier.getfeature(text))
			train_y.append(0)
		self.classifier.trainclassifier(train_x,train_y)
		return self.classifier
class GetCategory(object):
	def __init__(self):
		self.classifier = {}
		for cate in cates:
			self.classifier[cate] = ModelClass(cate).train(1000,100)
	def get_categorys(self,text):
		categorys = []
		for cate in cates:
			model = self.classifier(cate)
			feature = model.getfeature(text)
			result = model.getresuslt(feature)[0]
			if result == 1:
				categorys.append(cate)
		if categorys == []:
			return ["other"]
		return categorys

'''
if __name__=="__main__":
	client = mongocli.MongoCli()
	cd = creatdata.CreatData()
	cf = classifier.Classifier()
	collection = client.getdata("mydb","web")
	cd.setcollection(collection)
	#train vectorizer
	Text_number = 100
	corpus_vec = []
	for cate in cates:
		text = cd.getTextData(Text_number,cate)
		if text == None:
			print "get Fial..."
		print "%s number is %d...."%(cate,len(text))
		corpus_vec.extend(text)
	cf.trainvectorizer(corpus_vec)
	print "train vectorizer %d"%len(corpus_vec)
	#train classifier category
	category = "Sports"
	Train_number = 100
	Train_X = []
	Train_Y = []

	texts = cd.getTextData(Train_number*10,category)
	if texts == None:
		print "%s getTextData fail...."
	print "train classifier +munber is %d...."%len(texts)
	for text in texts:
		feature = cf.getfeature(text)
		Train_X.append(feature)
		Train_Y.append(1)
	texts = []
	for cate in cates:
		if cate == category:
			continue
		t = cd.getTextData(Train_number,cate,category)
		if t == None:
			print "%s getTextData fail...."%cate
			continue
		texts.extend(t)
	print "train classifier -number is %d...."%len(texts)
	for text in texts:
		feature = cf.getfeature(text)
		Train_X.append(feature)
		Train_Y.append(0)
	cf.trainclassifier(Train_X,Train_Y)
	print "test is start...."
	
	texts = cd.getTextData(11000,'Sports',category)
	feature = []
	count = 0
	right = 0
	wrong = 0
	for text in texts:
		count = count + 1
		if count <= 10000 :
			continue
		feature = cf.getfeature(text)
		ret = cf.getresult(feature)[0]
		if ret == 1:
			right = right + 1
		else:
			wrong = wrong + 1
	print right,wrong
	print feature
	print "train classifier %d"%len(Train_X)
	print "game over...."
'''
