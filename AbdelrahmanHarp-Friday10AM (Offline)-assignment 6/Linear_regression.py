import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from sklearn.model_selection import learning_curve
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error,mean_squared_error




# Read Fill

ecome = pd.read_csv("D:/Data/Ecommerce Customers.csv")
print(ecome.head())
print(ecome.info())
print(ecome.describe())
print(ecome.isnull().sum())
col = ['Email', 'Address', 'Avatar']
ecome.drop(columns=col, inplace=True)
# print(ecome.head())
# sns.lmplot(x='Length_of_Membership', y='Yearly_Amount_Spent', data=ecome)
y = ecome.Yearly_Amount_Spent
# print(y.head())
ecome.drop(columns=["Yearly_Amount_Spent"], inplace=True)
x = ecome.copy()

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=101)
lr_model = LinearRegression()
lr_model.fit(x_train, y_train)
y_pred =lr_model.predict(x_test)
print(ecome.iloc[5].values)
print(lr_model.predict([[33.87103788, 12.02692534, 34.47687763,  5.4935072]]))
print(y.iloc[5])
# test Quality for model train
print('Mean Absolute Error:', mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(mean_squared_error(y_test, y_pred)))
print('R^2 Score:', r2_score(y_test, y_pred))
# print(plt.hist(ecome))
# sns.distplot(y_test-y_pred, bins = 50);
sns.histplot((y_test-y_pred), bins=50)
# plt.hist((y_test-y_pred))
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Histogram of Residuals')
plt.show()
