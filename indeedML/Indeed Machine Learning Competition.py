# -*- coding: utf-8 -*-
import writeToFile as wtf
import trainingTagSplit as ts
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

from sklearn.linear_model import RidgeClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.ensemble import RandomForestClassifier

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer

train=pd.read_csv('indeed_ml_dataset/train.tsv',sep='\t')
test=pd.read_csv('indeed_ml_dataset/test.tsv',sep='\t')


#X_train, X_test,y_train,y_test = train_test_split(train, test_size = 0.2)

def predictTag(df,splitByTagMethod,clf,vect):
    ch2=SelectKBest(chi2,k='all')
    trainPayPeriodSplit = splitByTagMethod(train.to_dict(orient='dict'))
    vectorizer = vect
    X_train = vectorizer.fit_transform(trainPayPeriodSplit['description'].values)
    y_train=trainPayPeriodSplit['tags'].values
    X_train = ch2.fit_transform(X_train, y_train)
    classifier = clf
    classifier.fit(X_train,y_train)
    X_test=vectorizer.transform(df['description'].values)
    X_test = ch2.transform(X_test)
    prediction = classifier.predict(X_test)
    return prediction

def main(df,clfMultiClass,clfBinaryClass):
    licence_result=predictTag(df,ts.splitByLicenceTags,clfBinaryClass,TfidfVectorizer(sublinear_tf=False,max_df=0.7,stop_words='english',ngram_range=(1,2)))
    supervising_result=predictTag(df,ts.splitBySupervisingTags,clfBinaryClass,TfidfVectorizer(sublinear_tf=False,max_df=0.7,stop_words='english',ngram_range=(1,2)))
    education_result=predictTag(df,ts.splitByEducationTags,clfMultiClass,TfidfVectorizer(sublinear_tf=True,max_df=0.7,stop_words='english',ngram_range=(1,2)))
    exp_result=predictTag(df,ts.splitByExperienceTags,clfMultiClass,TfidfVectorizer(sublinear_tf=True,max_df=0.7,stop_words='english',ngram_range=(1,2)))
    time_result=predictTag(df,ts.splitByTimeTags,clfMultiClass,TfidfVectorizer(sublinear_tf=True,max_df=0.7,stop_words='english',ngram_range=(1,2)))
    payPeriod_result=predictTag(df,ts.splitByPayPeriodTags,clfMultiClass,TfidfVectorizer(sublinear_tf=True,max_df=0.7,stop_words='english',ngram_range=(1,2)))
    wtf.combineArrayAndWriteToFile(licence_result, supervising_result, education_result, exp_result, time_result,payPeriod_result)

main(test,SGDClassifier(loss="modified_huber",penalty="l1",n_iter=50),NearestCentroid())

print 'QED'

# testing accuracy:
# from sklearn import metrics
# metrics.accuracy_score(testData,prediction) #percent correct (try to beat the null accuracy)
# metrics.confusion_matrix(testData,prediction)
# #[true_neg false_pos],
# #[false_ned true_pos]