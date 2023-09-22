import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from sklearn.model_selection import learning_curve
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# set data in my file project

salary_data = pd.read_csv("D:/data/Salary_dataset.csv")
print(salary_data.head(10))
# print(salary_data.isnull().sum())
# print(salary_data.isnull().any())
print(salary_data.info())
print(salary_data.describe())

salary_data.drop(columns=("Unnamed: 0"), inplace=True)
print(salary_data.head(10))
print(salary_data.describe())
y = salary_data.Salary
x = salary_data.copy()

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
print(x_train.shape)
print(x_test.shape)
# print(y_train.shape)
# print(y_test.shape)

lr_model = LinearRegression()
lr_model.fit(x_train, y_train)
y_pred = lr_model.predict(x_test)
print(salary_data.iloc[1].values)
print(lr_model.predict([[1.4000e+00, 4.6206e+04]]))
print(y.iloc[1])
salary_data.hist()
plt.show()
