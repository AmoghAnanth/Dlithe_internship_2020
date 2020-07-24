# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:55:23 2020

@author: Amogh A N
"""

import pandas as pd
#getting data from the dektop
data = pd.read_csv("C:/Users/Amogh A N/Desktop/workshop/Python_Dataset/assignment/usedcars.csv")

#data cleansing
#drop not so important data
data.drop(["v.id"],inplace=True,axis=1)
data.info()

#pictorial relation of data/data analysis
import seaborn as sb
sb.heatmap(data.corr(),annot=True,vmin=0.5,vmax=0.7,cmap='coolwarm',linewidth=3,linecolor='red')
sb.pairplot(data)

#setting and x and y arrays
#iv: distance, fueltype,Manufacturingyear,Price in inr
#tv: Maker
x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

#split universal dataset(train:test)
#library:sklearn
#module:model_selection
#class : train_test_split
from sklearn.model_selection import train_test_split as tts
x_train,x_test,y_train,y_test = tts(x,y,test_size=0.3,random_state=350)
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
#check accuracy by giving x_test and y_test data
accuracy = model_linreg.score(x_test,y_test)
print("Linear Regression Accuracy:", accuracy)
#Checking the accuracy
#Library: sklearn
#module : metrics
#class  : r2score
#r2score(actual, predicted)
from sklearn.metrics import r2_score as r2s
cm = r2s(y_test, y_pred)