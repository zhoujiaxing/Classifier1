from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

class Classifier(object):
	def __init__(self):

		self.classifier = LogisticRegression()
		self.vectorizer = TfidfVectorizer()
	
	def trainvectorizer(self,corpus):
		
		self.vectorizer.fit_transfrom(corpus)
		print "vectrizer train is over...."


	def trainclassifier(self,train_X,train_Y):
		
		self.classifier.fit(train_X,train_Y)
		print "classifier train is over ...."

	def getferture(self,text):#return a feature array
		
		tfidf = self.vectorizer.transfrom(text)
		matrx = tfidf.toarray()
		array = matrx[0]
		return array
		
	def getresult(self,feature):#return true or false
		
		return self.classifier.predict(feature)