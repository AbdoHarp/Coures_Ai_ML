import pandas as pd
import numpy as np
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


data = pd.read_csv("D:/Data/loan_data.csv")

# print(data.head())
print(data.shape)
print(data.info())
# print(data.isnull().sum())

# sns.pairplot(data, hue='purpose', palette='Set3')


x = data.drop("purpose", axis=1)
y = data["purpose"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# print(x_train.shape)
# print(x_test.shape)
# print(y_train.shape)
# print(y_train.shape)

ds_model = DecisionTreeClassifier()
ds_model.fit(x_train, y_train)
ds_y_pred = ds_model.predict(x_test)
# print(ds_y_pred)
print(classification_report(y_test, ds_y_pred))
# cm = confusion_matrix(y_test, ds_y_pred)
# sns.heatmap(cm, annot=True)
print(y_test.value_counts())
params = {
    "criterion": ["gini", "entropy"],
    "max_depth": list(range(1, 40))
}
gs = GridSearchCV(ds_model, params, cv=5)
gs.fit(x_train, y_train)
print(gs.best_params_)
print(gs.best_score_)
plt.figure(figsize=(20, 20))
# tree.plot_tree(ds_model.fit(x_train,y_train))


plt.show()