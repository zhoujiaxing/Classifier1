from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from pymongo import MongoClient
import pymongo
import creatdata
import classifier
import mongocli


cates=["Auto","Business","Cricket","Entertainment/Bollywood","Health","Lifestyle","National","Politics","Sports","Technology","World"]


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
