# regression ---> predict value
# model ---> 1- math 2- stat(error)
#  math model = y= mx + b
# 2- stat model = y = Bx + BO + E
# linear regression model ---> predict value

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from sklearn.model_selection import learning_curve
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("D:/data/data (1).csv")
# print(df.isnull().sum())

# split data ----> 1- train
# 2- test
# split data x and y

y = df.Price
# df.drop(columns=["Price", "Address"], inplace=True)
# # print(df)
# x = df.copy()
# # print(x)
# #
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# print(x_train.shape)
# print(x_test.shape)
#
# lr_model = LinearRegression()
# lr_model.fit(x_train, y_train)
# y_pred = lr_model.predict(x_test)
# print(df.iloc[1].values)
# print((lr_model.predict([[7.92486425e+04, 6.00289981e+00, 6.73082102e+00, 3.09000000e+00, 4.01730722e+04]])))
# print(y.iloc[1])
# df.hist()



# data = pd.read_csv("D:/Data/data (1).csv")
# # data.info()
# # data.isnull().any()
# #
# y= data.Price
# # y.head()
# x=data.copy()
# x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
# # use model
# lr_model = LinearRegression()
# # fit model
# lr_model.fit(x_train,y_train)
# y_pred = lr_model.predict(x_test)
# data.iloc[5].values


df = pd.read_csv("D:/Data/train (2).csv")
df.head()
# df.info()
df.isnull().sum()

cols = ["PassengerId","Name","Ticket","Fare","Cabin"]
df.drop(columns= cols ,inplace = True)
df.head()
df.isnull().sum()
df["Embarked"].unique()

# sex_mapping = {"male":1, "female":0}
# df.Sex = df.Sex.map(sex_mapping)
# print(df.head())
Embarked_mapping = {"s":0,"c":1,"s":2,"nan":3}
df.Embarked = df.Embarked.map(Embarked_mapping)
print(df.head())
