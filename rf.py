# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 09:31:12 2019

@author: DHRUVIL
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

iris=load_iris()
X=iris.data
y=iris.target

X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=100, test_size=0.3)

model=RandomForestClassifier(n_estimators=10)
model.fit(X_train,y_train)
predicted=model.predict(X_test)

print(accuracy_score(predicted,y_test))

import pickle #Saves python objects as binary file
with open('C:/Users/DHRUVIL/Desktop/Deploying ML models/rf_model.pkl','wb') as model_pkl:
    pickle.dump(model,model_pkl)
