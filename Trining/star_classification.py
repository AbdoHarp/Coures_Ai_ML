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



star_gender = pd.read_csv("D:/data/gender_classification_v7.csv")

print(star_gender.head())
print(star_gender.info())
# print(star_gender.describe())
# print(star_gender.isnull().any())
# print(star_gender.isnull().sum())

# sns.pairplot(star_gender, hue='gender')

y = star_gender.distance_nose_to_lip_long
# print(y )
star_gender.drop(columns='distance_nose_to_lip_long', inplace=True)
genderType = {"Male": 1, "Female": 0}
star_gender.gender = star_gender.gender.map(genderType)
print(star_gender)
x = star_gender.copy()
scaler = StandardScaler()
x = scaler.fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# //////////////////////////// GaussianNB model train ///////////////////////////////
# gns_model = GaussianNB()
# gns_model.fit(x_train, y_train)
# gns_y_pred = gns_model.predict(x_test)
# print(classification_report(y_test, gns_y_pred))
# cm = confusion_matrix(y_test, gns_y_pred)
# sns.heatmap(cm, annot=True)

# ////////////////////////// KNeighborsClassifier model train /////////////////////////////////
# knn_model = KNeighborsClassifier()
# knn_model.fit(x_train, y_train)
# knn_y_pred = knn_model.predict(x_test)
# print(classification_report(y_test, knn_y_pred))
# cm = confusion_matrix(y_test, knn_y_pred)
# sns.heatmap(cm, annot=True)

# ////////////////////////////////// LinearRegression model train //////////////////////
# lr_model = LinearRegression()
# lr_model.fit(x_train, y_train)
# lr_y_pred = lr_model.predict(x_test)
# print(star_gender.iloc[5].values)
# print(lr_model.predict([[ 1.,  13.,   6.8,  1.,   1.,   1.,   1.]]))
# print(y.iloc[5])
# print(r2_score(y_test, lr_y_pred))
# print(mean_absolute_error(y_test, lr_y_pred))
# print(mean_squared_error(y_test, lr_y_pred))
# print('Root Mean Squared Error:', np.sqrt(mean_squared_error(y_test, lr_y_pred)))
# plt.hist((y_test, lr_y_pred))
# plt.xlabel("distance nose")
# plt.ylabel("lip long")
# plt.title('distance nose to lip long')

# ///////////////////////////////// LogisticRegression model Train ///////////////////////////
# lg_model = LogisticRegression()
# lg_model.fit(x_train, y_train)
# lg_y_pred = lg_model.predict(x_test)
#
# print(r2_score(y_test, lg_y_pred))
# print(mean_absolute_error(y_test, lg_y_pred))
# print(mean_squared_error(y_test, lg_y_pred))
# print('Root Mean Squared Error:', np.sqrt(mean_squared_error(y_test, lg_y_pred)))
# print(classification_report(y_test, lg_y_pred))
# cm = confusion_matrix(y_test, lg_y_pred)
# sns.heatmap(cm, annot=True)

plt.show()
