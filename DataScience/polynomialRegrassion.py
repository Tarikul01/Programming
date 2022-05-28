import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import  r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
df=pd.read_csv('Startups.csv')

regration=LinearRegression()
# regration.fit(df[['RDSpend','Administration','MarketingSpend']].values,df.Profit)
# profit=regration.predict([[15000,16000,17000]])
x=df.drop(['Profit'],axis=1)

y=df['Profit']
State=pd.get_dummies(x['State'],drop_first=True)
x=x.drop("State",axis=1)
x=pd.concat([x,State],axis=1)
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=.30,random_state=1)
# print(xtrain)
sc=StandardScaler()
sc.fit(xtrain)
x_train=sc.transform(xtrain)
x_test=sc.transform(xtest)
# print(x_test)
poly_reg=PolynomialFeatures(degree=2)
poly_reg.fit(x_train)
x_train_poly=poly_reg.transform(x_train)
x_test_poly=poly_reg.transform(x_test)
# print(x_test_poly)
# x_train=sc.transform(xtrain)
# x_test=sc.transform(xtest)
# poly_reg=PolynomialFeatures(degree=2)
# poly_reg.fit(x_train)
# x_train_poly=poly_reg.transform(x_train)
# x_test_poly=poly_reg.transform(x_test)
regration.fit(x_train_poly,ytrain)

performance=regration.score(x_test_poly,ytest)
# print(performance)

# predict  profit
pr=regration.predict([x_test_poly[0,:]])
pr1=regration.predict(x_test_poly)
mse=mean_squared_error(ytest,pr1)
rmse=np.sqrt(mse)
print(mse,rmse)