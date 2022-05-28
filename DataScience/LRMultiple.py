import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import  r2_score
df=pd.read_csv('Startups.csv')
# print(df)
# print(df['R&D Spend'])
# calculate mean value
# admenavalue=df.Administration.mean()
# df.Administration.fillna(admenavalue)
regration=LinearRegression()
regration.fit(df[['RDSpend','Administration','MarketingSpend']].values,df.Profit)
profit=regration.predict([[15000,16000,17000]])
x=df.drop(['Profit'],axis=1)
y=df['Profit']
# print(y)

 # encoading  convert a column into categorial  column

State=pd.get_dummies(x['State'],drop_first=True)
# print(State)

x=x.drop("State",axis=1)
x=pd.concat([x,State],axis=1)
# print(x)
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=.50,random_state=1)
regration.fit(xtrain,ytrain)
predictvalue=regration.predict(xtest)

 # Determind performance ration use r _ scrore
score=r2_score(ytest,predictvalue)

# Another way check performance
score1=regration.score(xtest,ytest)
print(score1)



# coeficient=regration.coef_
# interception=regration.intercept_