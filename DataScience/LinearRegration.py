import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv('auto_insurance_sweden.csv')
x=df[['No_of_claim']]
y=df['payment']
# df.head()   //use for first 5 data
# print(y.head(3)) print first three data
# df.shape use for print shape
# df.isnull().any()  or df.isnull().sum() show null value
# plt.scatter(df['number of claims'],df['total payment for all the claims']) use for show data visulization
# scatter use for graphicla view  in graphs
# plt.scatter(x,y)
# hist use for tabular view  in graph
# plt.hist(x,bins=30,color='pink')
# plt.title("claim VS payment for all claims")
# plt.xlabel('claims')
# plt.ylabel('Payment')
# plt.show()
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=.50,random_state=1)
regration=LinearRegression()
# print(xtrain)
regration.fit(xtrain.values,ytrain)
pd=regration.predict(xtest.values)
print(pd)
# print(df['number of claims'].shape)
# print(type(xtest)
# print(xtest.to_numpy())
# print(regration.predict(xtest))
# plt.scatter(x,y,marker='+',color='red')
# plt.plot(xtest.to_numpy(),regration.predict(xtest))
# plt.show()
# print(regration.predict([[30]]))