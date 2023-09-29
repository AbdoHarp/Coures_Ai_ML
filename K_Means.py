import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.cluster
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
from sklearn.cluster import KMeans

customers = pd.read_csv("D:/data/mallcustomers.csv")
print(customers.head())
print(customers.info())
print(customers.describe().T)

customers.drop(columns="CustomerID", inplace=True)
# print(customers.head())


# sns.boxplot(data=customers , x="Gender", y="Income")
# sns.boxplot(data=customers , x="Gender", y="Age")
# sns.boxplot(data=customers , x="Gender", y="SpendingScore")
# sns.scatterplot(data=customers , x="Age", y="Income",s=100)
# sns.scatterplot(data=customers , x="Income", y="SpendingScore",s=100 , hue="Gender")

sc = StandardScaler()
customers_scaled = sc.fit_transform(customers[["Income", "SpendingScore"]])
customers_scaled = pd.DataFrame(customers_scaled, columns=["Income", "SpendingScore"])
# print(customers.head())
# print(customers.describe().T)

km = KMeans(n_clusters=3, n_init=10, random_state=1234)
km.fit(customers_scaled)
print(km.labels_)
print(km.inertia_)
print(pd.Series(km.labels_).value_counts())
print(km.cluster_centers_)
cluster_cent = pd.DataFrame(km.cluster_centers_, columns=["Income", "SpendingScore"])
ax = sns.scatterplot(data=customers_scaled, x="Income", y="SpendingScore", hue=km.labels_,marker="x", alpha=0.8, s=120, legend=False)
ax= sns.scatterplot(data=cluster_cent, x="Income", y="SpendingScore", hue=cluster_cent.index, palette="colorblind", alpha=0.8, s=250, marker="v", legend=False)

for i in range(len(cluster_cent)):
    plt.text(x=cluster_cent.Income[i], y= cluster_cent.SpendingScore[i],s=i)

plt.show()
