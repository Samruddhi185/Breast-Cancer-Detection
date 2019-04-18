# -*- coding: utf-8 -*-
"""BreastCancerDetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Aggdo8kgzPqZSAsyzKnn2OXoMj4nvJT_
"""
#array-processing package
import numpy as np
#Simple and efficient tools for data mining and data analysis sklearn
from sklearn import preprocessing
#parameter tuning
from sklearn.model_selection import cross_validate
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.metrics import classification_report, accuracy_score
#data manipulation
from pandas.plotting import scatter_matrix
#plotting framework
import matplotlib.pyplot as plt
#data structures and data analysis tools
import pandas as pd

#loading dataset
url = "cancer.csv"
df = pd.read_csv(url)

#data cleaning missing values
df.replace('?',-9999, inplace= True)
print(df.shape)
#id useless column inplace=True, do operation inplace and return None
df.drop('id',1,inplace=True)
print(df.loc[0])


X=np.array(df.drop(['classes'],1))
y=np.array(df['classes'])
#random state = seed to get same results
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8)

scoring = 'accuracy'
models=[]
models.append(('KNN',KNeighborsClassifier(n_neighbors=5)))
models.append(('SVM',SVC()))

results=[]
names=[]

from sklearn.model_selection import KFold

for name, model in models:
  kfold = model_selection.KFold(n_splits=10, random_state=8)
  cv_results = model_selection.cross_val_score(model, X_train, y_train, cv=kfold, scoring=scoring)
  results.append(cv_results)
  names.append(name)
  msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
  print(msg)

for name, model in models:
  model.fit(X_train, y_train)
  pred = model.predict(X_test)
  print(name)
  print(accuracy_score(y_test, pred))
  print(classification_report(y_test, pred))