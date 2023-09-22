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
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer

loan_data = pd.read_csv("D:/data/loan.csv")
# print(loan_data.head())
# print(loan_data.describe())
# print(loan_data.info())


# X = loan_data[['Income', 'Loan Amount']]
# y = loan_data['Default']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=1234)

# rm_model = RandomForestClassifier()
# rm_model.fit(X_train, y_train)
#
# rm_y_pred = rm_model.predict(X_test)
# score = rm_model.score(X_test, y_test)
# print(score)
# param = {'max_depth': [2, 3, 4, 5], 'min_samples_split': [2, 3, 4], 'min_samples_leaf': [1, 2, 3, 4, 5, 6]}

# grid_search = GridSearchCV(estimator=rm_model, param_grid=param)
# grid_search.fit(X_train, y_train)
#
# model =grid_search.best_estimator_
# # print(model)
# model.fit(X_train, y_train)
# model.predict(X_test)
# print(model.score(X_train,y_train))
# print(model.score(X_test,y_test))



# param_grid = {'n_estimators': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
#             'learning_rate': [0.1, 0.2, 0.3, 0.4, 0.5],
# }
#
# ad_model = AdaBoostClassifier()
# ad_model.fit(X_train,y_train)
# ad_y = ad_model.predict(X_test)
# print(ad_model.score(X_train, y_train))
# print(ad_model.score(X_test, y_test))
# grid_search = GridSearchCV(estimator=ad_model, param_grid=param_grid)
# grid_search.fit(X_train, y_train)
# model_ad = grid_search.best_estimator_
# model_ad.fit(X_train, y_train)
# model_ad_y = model_ad.predict(X_test)
# print(grid_search.best_params_)
# print(model_ad.score(X_train, y_train))
# print(model_ad.score(X_test, y_test))


cancer = load_breast_cancer()

print(type(cancer))
print(cancer.keys())

df=pd.DataFrame(cancer["data"],columns=cancer["feature_names"])
# print(df.head())


df_target = pd.DataFrame(cancer["target"],columns=["cancer"])


X_train, X_test, y_train, y_test = train_test_split(df, df_target, test_size=0.3,random_state=101)

svc_liner_model = SVC(kernel="linear")
svc_liner_model.fit(X_train, y_train)
y_pred = svc_liner_model.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# svc_degree_model = SVC(kernel="poly", degree=3)
# svc_degree_model.fit(X_train, y_train)
# y_pred = svc_degree_model.predict(X_test)
# print(confusion_matrix(y_test, y_pred))
# print(classification_report(y_test, y_pred))

# pca


