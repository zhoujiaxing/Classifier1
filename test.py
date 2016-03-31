from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from pymongo import MongoClient
import pymongo
import creatdata
import classifier
import mongocli


cates=["Auto","Business","Cricket","Education","Entertainment","Health","Lifestyle","National","Politics","Sports","Technology","Top Stories","World"]


if __name__=="__main__":
	client = mongocli.MongoCli()
	cd = creatdata.CreatData()
	cf = classifier.Classifier()
	collection = client.getdata("hinews","article")
	cd.setcollection(collection)
	#train vectorizer
	Text_number = 100
	corpus_vec = []
	for cate in cates:
		text = cd.getTextData(Text_number,cate)
		if text == None:
			print "get Fial..."
		corpus_vec.extend(text)
	cf.trainvectorizer(corpus_vec)

	#train classifier category

	category = "Auto"
	Train_number = 100
	Train_X = []
	Train_Y = []

	texts = cd.getTextData(Train_number*12,category)
	if texts == None:
		print "%s getTextData fail...."
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
		texts.extend(t)
	for text in texts:
		feature =cf.getfeature(text)
		Train_X.append(feature)
		Train_Y.append(0)
	cf.trainclassifier(Train_X,Train_Y)
	print "game over...."
