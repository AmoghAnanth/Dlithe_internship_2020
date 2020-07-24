# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:48:59 2020

@author: Amogh A N
"""

import pandas as pd
import numpy as np
#reading the file from folder
data = pd.read_csv("C:/Users/Amogh A N/Desktop/workshop/Python_Dataset/assignment/store.csv")

#data processing
data = data.iloc[:, np.r_[3,0:3,4]]
data.info()
df = pd.get_dummies(data, prefix=['reps', 'product','region'], columns=['reps', 'product','region'])

#pictorial relation of data/data analysis
import seaborn as sb
sb.heatmap(df.corr(),annot=True,vmin=0.5,vmax=0.7,cmap='coolwarm',linewidth=3,linecolor='red')
sb.pairplot(df)

#setting and x and y arrays
#iv:reps,product,qty,region
#tv: revenue
x = df.iloc[:,1:].values
y = df.iloc[:,0].values

#split universal dataset(train:test)
#library:sklearn
#module:model_selection
#class : train_test_split
from sklearn.model_selection import train_test_split as tts
x_train,x_test,y_train,y_test = tts(x,y,test_size=0.3,random_state=2500)

#Algorithm selection
#Linear regression
#Library: sklearn
#module : Linear_model
#class  : LinearRegression
from sklearn.linear_model import LinearRegression as linreg
model_linreg = linreg()
#train the model. Use fit(training arrays)
model_linreg.fit(x_train,y_train)
y_pred = model_linreg.predict(x_test)

#Checking the accuracy
#Library: sklearn
#module : metrics
#class  : r2score
#r2score(actual, predicted)
from sklearn.metrics import r2_score as r2s
cm = r2s(y_test, y_pred)
