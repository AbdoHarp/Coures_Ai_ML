import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from sklearn.model_selection import learning_curve
from sklearn.impute import SimpleImputer


# df = pd.read_csv("D:/data/USA_cars_datasets.csv")
# df.drop(['Unnamed: 0'], axis=1,inplace=True)
# print(df.head())
# print(df.shape)
# print(df.info)
# print(df.describe())
# print(df.isnull().sum())
# print(df.isnull().any())
# # print(df.hist())
# #
# # # print(p)
# # plt.figure(figsize=(12,6))
# # sns.scatterplot(x= df["price"],y= df["mileage"])
# #
# # sorted_brand = df.groupby(["brand"])["price"].median().sort_values()
# # # print(sorted_brand)
# # plt.figure(figsize=(12,6))
# # sns.boxplot(x=df["brand"],y=df["price"], order = list(sorted_brand.index))
# # plt.xticks(rotation= 70)
#
# # df['state'].value_counts().head(10).plot(kind = "barh",figsize= (10,10))
# df["color"] = df["color"].astype("category")
# plt.figure(figsize=(15,8))
# sns.countplot(data=df, x="color")
# plt.xticks(rotation=90)

test = pd.read_csv("D:/data/test.csv")
# print(test.head())
# print(test.info)
# print(test.isnull().any)
# print(test.isnull().sum())
# print(test.describe)
train = pd.read_csv("D:/data/train.csv")
# print(train.head())
# print(train.info)
# print(train.isnull().any)
# print(train.isnull().sum())
# print(train.describe)
# train.drop(["Cabin"],inplace=True, axis=1)

# msno.bar(train)
# print(msno.bar(train))
# print(train)
# train_constant = train.copy()
# test_constant = test.copy()
# Simple_imputer = SimpleImputer(strategy="constant")
# train_constant.iloc[:, :] = Simple_imputer.fit_transform(train_constant)
# print(train_constant.isnull().sum())
# print(train_constant)
# test_constant.iloc[:, :] = Simple_imputer.fit_transform(test_constant)
# print(test_constant.isnull().sum())

cityDay = pd.read_csv("D:/data/city_day.csv")
# print(cityDay)
# print(cityDay.isnull().any())
# print(cityDay.isnull().sum())

# # forward Fill
# print(cityDay['Xylene'][50:64])
# cityDay.fillna(method="ffill", inplace=True)
# print(cityDay['Xylene'][50:64])
#
# # backFill
# cityDay.fillna(method="bfill", inplace=True)
# print(cityDay['Xylene'][50:64])
#
# print(cityDay.isnull().sum())





plt.show()
