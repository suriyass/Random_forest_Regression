#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import validation_curve
from sklearn.ensemble import RandomForestClassifier
data = pd.read_csv("dataset.csv")
data = data.fillna('')
data.head()
from sklearn.utils import shuffle
data = shuffle(data)
X = pd.DataFrame(data.iloc[:,:-1])
y = pd. DataFrame(data.iloc[:,-1])
X
y
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import accuracy_score 
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report 
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20)
from sklearn.ensemble import RandomForestRegressor 
Regressor = RandomForestRegressor(n_estimators=20,random_state=0)
Regressor.fit(X_train, y_train.values.ravel())
pred = Regressor.predict(X_test)
mae = metrics.mean_absolute_error(y_test,pred)
Accuracy = (100 - mae)
print('Accuracy:', round(Accuracy,2), '.%')
param_range = np.arange(1, 250, 2)
train_scores, test_scores = validation_curve(RandomForestClassifier(), 
                                             X, 
                                             y, 
                                             param_name="n_estimators", 
                                             param_range=param_range,
                                             cv=3, 
                                             scoring="accuracy", 
                                             n_jobs=-1)
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)
plt.plot(param_range, train_mean, label="Training score", color="black")
plt.plot(param_range, test_mean, label="Cross-validation score", color="red")
plt.fill_between(param_range, train_mean - train_std, train_mean + train_std, color="red")
plt.fill_between(param_range, test_mean - test_std, test_mean + test_std, color="green")
z_test =np.array([[0.300002, 3.900003,12200000.0, 16600000.0,60000]])
pre = Regressor.predict(z_test)
pre


