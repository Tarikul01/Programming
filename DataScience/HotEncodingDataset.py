import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import  r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
df=pd.read_csv('aluminium_prize.csv')

x=df.drop(['Month'],axis=1)
y=df['Price_alum']
month=pd.get_dummies(df['Month'],drop_first=True)
x=x.drop("Price_alum",axis=1)
print(month)

x=pd.concat([x,month],axis=1)
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=.50,random_state=1)
regration=LinearRegression()
sc=StandardScaler()
sc.fit(xtrain)
x_train=sc.transform(xtrain)
x_test=sc.transform(xtest)
regration.fit(x_train,ytrain)
# x_train_poly=regration.
# x_test_poly=poly_reg.transform(x_test)
# regration.fit(xtrain.values,ytrain.values)
# print(x_train)
pd=regration.predict(x_test)
score=regration.score(x_test,ytest)
rscore=r2_score(ytest,pd)
# print(rscore)
# print(score)

# print(regration.predict([[2022]]))