import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import learning_curve
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
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
# from sklearn.preprocessing import OrdinalEncoder
import category_encoders as ce
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# car = pd.read_csv("D:/data/car_evaluation.csv")
# print(car.head())
# # print(car.info())
# # print(car.isnull().any())
# # print(car.isnull().sum())
#
# col_name = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
# car.columns = col_name
# print(car.head())
# print(car["class"].unique())
# # for i in col_name:
# #     print(car[i].value_counts())
#
# y = car["class"]
# # print(y.head())
#
# car.drop(columns=["class"], inplace=True)
# # print(car.head())
# x = car.copy()
#
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)
#
# encoder = ce.OrdinalEncoder()
# x_train = encoder.fit_transform(x_train)
# x_test = encoder.transform(x_test)
# # print(x_train.head())
# ds_model = DecisionTreeClassifier()
# ds_model.fit(x_train, y_train)
# y_pred = ds_model.predict(x_test)
# cm = confusion_matrix(y_test, y_pred)
# sns.heatmap(cm, annot=True)
# print(y_test.value_counts())
# print(classification_report(y_test,y_pred))
# params = {
#     "criterion": ["gini", "entropy"],
#     "max_depth": list(range(1, 40))
# }
# gs = GridSearchCV(ds_model, params, cv=5)
# gs.fit(x_train, y_train)
# print(gs.best_params_)
# print(gs.best_score_)
# plt.figure(figsize=(20,20))
# tree.plot_tree(ds_model.fit(x_train,y_train))
#

#
# drug = pd.read_csv("D:/data/drug200.csv")
#
# print(drug.head())
# # print(drug.info())
# # print(drug.isnull().sum())
# print(drug["Drug"].unique())
# # for i in drug:
# #     print(drug[i].value_counts())
# y = drug["Drug"]
# drug.drop(columns=["Drug"], inplace=True)
# x = drug.copy()
# encoder = LabelEncoder()
# for col in x.columns:
#     x[col] = encoder.fit_transform(x[col])
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# # encoder = ce.OrdinalEncoder()
# # x_train = encoder.fit_transform(x_train)
# # x_test = encoder.transform(x_test)
#
#
# de_model = DecisionTreeClassifier(criterion="entropy")
# de_model.fit(x_train, y_train)
# y_pred = de_model.predict(x_test)
#
# cm = confusion_matrix(y_test, y_pred)
# sns.heatmap(cm, annot=True)
# print(y_test.value_counts())
# print(classification_report(y_test, y_pred))
# tree.plot_tree(de_model.fit(x_train,y_train))


mushrooms = pd.read_csv("D:/data/mushrooms.csv")
print(mushrooms.head())
# print(mushrooms.info())
# print(mushrooms.isnull().sum())
#
y = mushrooms.Class
# print(y.head())
mushrooms.drop(columns=["Class"], inplace=True)
# print(mushrooms.head())
x = mushrooms.copy()
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)
print(y)
for col in x.columns:
    x[col] = label_encoder.fit_transform(x[col])
# print(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# ds_model = DecisionTreeClassifier(criterion="gini", max_depth=10)
# ds_model.fit(x_train, y_train)
# y_pred = ds_model.predict(x_test)
# cm = confusion_matrix(y_test, y_pred)
# sns.heatmap(cm, annot=True)
# print(classification_report(y_test, y_pred))
# ds_model = DecisionTreeClassifier(criterion="entropy", max_depth=10)
# ds_model.fit(x_train, y_train)
# y_pred = ds_model.predict(x_test)
# cm = confusion_matrix(y_test, y_pred)
# sns.heatmap(cm, annot=True)
# print(classification_report(y_test, y_pred))

# ds_model = DecisionTreeClassifier(random_state=42)
# ds_model.fit(x_train, y_train)
# y_pred = ds_model.predict(x_test)
# cm = confusion_matrix(y_test, y_pred)
# sns.heatmap(cm, annot=True)
# print(classification_report(y_test, y_pred))
# params = {
#     "criterion": ["gini", "entropy"],
#     "max_depth": list(range(1, 40))
# }
# gs = GridSearchCV(ds_model, params, cv=5)
# gs.fit(x_train, y_train)
# print(gs.best_params_)
# print(gs.best_score_)
# plt.show()


