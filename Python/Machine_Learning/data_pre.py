import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data_set = pd.read_csv(r'D:\ML\MachineLearningA-Z\Part1-DataPreprocessing\DataPreprocessing\Data.csv')
#print(data_set)
X= data_set.iloc[:,:-1].values
Y = data_set.iloc[:,3].values
# print (type(X))
# print (type(Y))



from sklearn.preprocessing import Imputer

imp = Imputer(missing_values='NaN',
              strategy='mean',
              axis=0
              )
imp = imp.fit(X[:, 1:3])

X[:,1:3] = imp.transform(X[:,1:3])


#print(X)

from sklearn.model_selection import train_test_split