import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from sklearn.model_selection import learning_curve
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder



#
# Titanic = pd.read_csv("D:/data/Titanic_new.csv")
# print(Titanic.head())
# # print(Titanic.info())
# # print(Titanic.isnull().sum())
#
# y = Titanic.Survived
# # print(y.head())
#
#
#
# col =['Unnamed: 0',"Survived"]
# Titanic.drop(columns=col, inplace=True)
# print(Titanic.head())
# x = Titanic.copy()
#
# sc = StandardScaler()
# x = sc.fit_transform(x)
#
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# knn_model = KNeighborsClassifier()
# # fit
# knn_model.fit(x_train, y_train)
# # preidct
# y_pred = knn_model.predict(x_test)
# # classification_report
# print(classification_report(y_test, y_pred))
# cm = confusion_matrix(y_test, y_pred)
# # sns.heatmap(cm, annot=True)
#
# score = []
# for i in range(1, 40):
# #model
#     knn_model = KNeighborsClassifier(n_neighbors=i)
#     knn_model.fit(x_train, y_train)
#     score.append(knn_model.score(x_test, y_test))
# plt.plot(range(1, 40), score)
# knn_model = KNeighborsClassifier()
# parmam = {
#     "n_neighbors": list(range(1, 40)),
#     "p": [1, 2]
# }
# gs = GridSearchCV(knn_model, parmam, cv=5)
# gs.fit(x_train, y_train)
# print(gs.best_params_)
# print(gs.best_score_)


# Example 2

# Iris = pd.read_csv("D:/data/Iris.csv")
# print(Iris.head(5))
# print(Iris.info())
# print(Iris.isnull().sum())
#
# y = Iris.Species
# # print(y.head())
# Iris.drop(columns=['Species', "Id"], inplace=True)
# x = Iris.copy()
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# # knn model
# knn_model = KNeighborsClassifier()
# knn_model.fit(x_train, y_train)
# y_pred = knn_model.predict(x_test)
# print(classification_report(y_test, y_pred))
# cm = confusion_matrix(y_test, y_pred)
# sns.heatmap(cm, annot=True)
# parmam = {
#     "n_neighbors": list(range(1, 40)),
#     "p": [1, 2]
# }
# gs = GridSearchCV(knn_model, parmam, cv=5)
# gs.fit(x_train, y_train)
# print(gs.best_params_)
# print(gs.best_score_)

# knnal = pd.read_csv("D:/data/KNNAlgorithmDataset.csv")
# print(knnal.head())
# # print(knnal.info())
# # print(knnal.isnull().sum())
#
# df_upd = pd.get_dummies(knnal, {'diagnosis'})
# x = df_upd.drop(['id', 'Unnamed: 32', 'diagnosis_B', 'diagnosis_M'], axis=1)
# y = df_upd['diagnosis_B']
#
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# scaler = StandardScaler()
# x_train = scaler.fit_transform(x_train)
# x_test = scaler.fit_transform(x_test)
# knn_model = KNeighborsClassifier()
# knn_model.fit(x_train, y_train)
# y_pred = knn_model.predict(x_test)
# print(classification_report(y_test, y_pred))
# cm = confusion_matrix(y_test, y_pred)
# sns.heatmap(cm, annot=True)
# parmam = {
#     "n_neighbors": list(range(1, 30)),
#     "p": [1, 2]
# }
# gs = GridSearchCV(knn_model, parmam, cv=5)
# gs.fit(x_train, y_train)
# print(gs.best_params_)
# print(gs.best_score_)


# y= Titanic.Survived
# Titanic.drop(columns=['Survived', "Unnamed: 0"],inplace=True)
# x =Titanic.copy()
# scaler = StandardScaler()
# x =scaler.fit_transform(x)
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
#
# gnb_model = GaussianNB()
# gnb_model.fit(x_train,y_train)
# gnb_y_pred =gnb_model.predict((x_test))
#
# print(classification_report(y_test,gnb_y_pred))
# cm = confusion_matrix(y_test,gnb_y_pred)
# # sns.heatmap(cm, annot=True)
#
# lr_model = LogisticRegression()
# lr_model.fit(x_train, y_train)
# lr_y_pred = lr_model.predict(x_test)
# print(classification_report(y_test, lr_y_pred))
# cm = confusion_matrix(y_test, lr_y_pred)
# sns.heatmap(cm, annot=True)




# mushrooms = pd.read_csv("D:/data/mushrooms.csv")
# print(mushrooms.head())
# # print(mushrooms.info())
# # print(mushrooms.isnull().sum())
# #
# y = mushrooms.Class
# # print(y.head())
# mushrooms.drop(columns=["Class"], inplace=True)
# # print(mushrooms.head())
# x = mushrooms.copy()
# label_encoder = LabelEncoder()
# y = label_encoder.fit_transform(y)
# # print(y)
# for col in x.columns:
#     x[col] = label_encoder.fit_transform(x[col])
# # print(x)
#
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)
#
# gnb_model = GaussianNB()
# gnb_model.fit(x_train,y_train)
# gnb_y_pred =gnb_model.predict((x_test))
#
# print(classification_report(y_test,gnb_y_pred))
# cm = confusion_matrix(y_test,gnb_y_pred)
# sns.heatmap(cm, annot=True)
# lr_model = LogisticRegression()
# lr_model.fit(x_train, y_train)
# lr_y_pred = lr_model.predict(x_test)
# print(classification_report(y_test, lr_y_pred))
# cm = confusion_matrix(y_test, lr_y_pred)
# sns.heatmap(cm, annot=True)


user_data = pd.read_csv("D:/data/User_Data (1).csv")
print(user_data.head())
# print(user_data.info())
# print(user_data.isnull().sum())

y = user_data.Purchased
# print(y)
user_data.drop(columns=["User ID", "Purchased"],inplace=True)
gender_mapping = {"Male": 1, "Female": 0}
user_data.Gender = user_data.Gender.map(gender_mapping)
print(user_data)
x = user_data.copy()
scaler = StandardScaler()
x = scaler.fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

gnb_model = GaussianNB()
gnb_model.fit(x_train, y_train)
gnb_y_pred = gnb_model.predict(x_test)

print(classification_report(y_test, gnb_y_pred))
cm = confusion_matrix(y_test, gnb_y_pred)
sns.heatmap(cm, annot=True)

lr_model = LogisticRegression()
lr_model.fit(x_train, y_train)
lr_y_pred = lr_model.predict(x_test)
print(classification_report(y_test, lr_y_pred))
cm = confusion_matrix(y_test, gnb_y_pred)
sns.heatmap(cm, annot=True)

# scaler = StandardScaler()
# x_train = scaler.fit_transform(x_train)
# x_test = scaler.fit_transform(x_test)
knn_model = KNeighborsClassifier()
knn_model.fit(x_train, y_train)
y_pred = knn_model.predict(x_test)
print(classification_report(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True)
parmam = {
    "n_neighbors": list(range(1, 30)),
    "p": [1, 2]
}
gs = GridSearchCV(knn_model, parmam, cv=5)
gs.fit(x_train, y_train)
print(gs.best_params_)
print(gs.best_score_)
plt.show()
