# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 18:52:06 2019

@author: 212757215
"""

#General imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Read the data csv
my_data =  pd.read_csv(r'D:\ML\MachineLearningA-Z\Part1-DataPreprocessing\DataPreprocessing\Data.csv')
X = my_data.iloc[:,:-1].values
y = my_data.iloc[:,-1].values

#Fill missing values
from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy = "mean",axis = 0)
imp = imp.fit(X[:,1:3])
X[:,1:3] = imp.transform(X[:,1:3])

#Encode data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
label_X = LabelEncoder()
X[:,0] = label_X.fit_transform(X[:,0])
onehot = OneHotEncoder(categorical_features=[0])
X = onehot.fit_transform(X).toarray()

label_y = LabelEncoder()
y = label_y.fit_transform(y)

#split data
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.2, random_state =0)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X =  StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


import copy

l = [1,[2,3],4,5,6]

l1= copy.deepcopy(l)
l1[1][0] = 6

print (l)
print (l1)