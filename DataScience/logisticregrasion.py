import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
df=pd.read_csv('diabetes2.csv')
x=df[['BMI']]
y=df['Outcome']
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=.70,random_state=1)
lr=LogisticRegression()
lr.fit(xtrain.values,ytrain)
pd=lr.predict(xtest.values)
pd1=lr.predict([[40]])
# print(lr.score(xtest,ytest))
print(pd1)