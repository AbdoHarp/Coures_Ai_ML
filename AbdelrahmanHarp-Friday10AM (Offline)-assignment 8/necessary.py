import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
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

data = pd.read_excel("D:/data/data.xlsx")

lab = LabelEncoder()
data["Class"] = lab.fit_transform(data["Class"])

print(data.head())
# print(data.info())
# print(data.isnull().sum())
# sns.pairplot(data, hue='Class')
sns.heatmap(data.corr(), annot=True)
#
y = data['Class']
x = data.drop('Class', axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
knn_model = KNeighborsClassifier()
knn_model.fit(x_train, y_train)
y_pred = knn_model.predict(x_test)

# Printing the Classification Report and Confusion Matrix
print("Classification Report (KNN):")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix (KNN):", cm)
# sns.heatmap(cm, annot=True)
parmam = {

    "n_neighbors": list(range(1, 30)),
    "weights": ["uniform", "distance"]
}
# parmam = {
#    'n_neighbors': [3, 5, 7],
#     'weights': ['uniform', 'distance']
# }
gs = GridSearchCV(knn_model, parmam, cv=5)
gs.fit(x_train, y_train)
print(gs.best_params_)
print(gs.best_score_)

gsa_model = GaussianNB()
gsa_model.fit(x_train,y_train)
gs_y_pred = gsa_model.predict(x_test)

print("Classification Report (Naive Bayes):")
print(classification_report(y_test, gs_y_pred))

cm = confusion_matrix(y_test, gs_y_pred)
print("Confusion Matrix (Naive Bayes):", cm)
# sns.heatmap(cm, annot=True)

plt.show()
