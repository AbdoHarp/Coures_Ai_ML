import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix




advertising = pd.read_csv("D:/data/advertising (1).csv")
print(advertising.head(5))
# print(advertising.info())
# print(advertising.describe())
print(advertising.isnull().any())
# print(advertising.isnull().sum())
# -----------------------------------------------------------------------------
# Create a jointplot showing Area Income versus Age.
# Create a jointplot showing the kde distributions of Daily Time spent on site vs. Age.
# Create a jointplot of 'Daily Time Spent on Site' vs. 'Daily Internet Usage'

# sns.histplot(advertising['Age'], bins=30)
# sns.jointplot(x='Age', y='Area Income', data=advertising)
# sns.jointplot(x='Age', y='Daily Time Spent on Site', data=advertising, kind='kde')
# sns.jointplot(x='Daily Time Spent on Site', y='Daily Internet Usage',  data=advertising)
# -----------------------------------------------------------------------------------


y = advertising.Clicked_on_Ad
advertising.drop(columns=["Clicked_on_Ad", "Ad Topic Line", "City", "Male", "Country", "Timestamp"], inplace=True)
x = advertising.copy()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
lg_model = LogisticRegression()
lg_model.fit(x_train, y_train)
lg_y_pred = lg_model.predict(x_test)

# ---------------------------------------------------------------------
# print('Mean Absolute Error:', mean_absolute_error(y_test, lg_y_pred))
# print('Mean Squared Error:', mean_squared_error(y_test, lg_y_pred))
# print('Root Mean Squared Error:', np.sqrt(mean_squared_error(y_test, lg_y_pred)))
# print('R^2 Score:', r2_score(y_test, lg_y_pred))
# --------------------------------------------------------------------
print(classification_report(y_test, lg_y_pred))
cm = confusion_matrix(y_test, lg_y_pred)
# print(cm)
sns.heatmap(cm, annot=True)




plt.show()