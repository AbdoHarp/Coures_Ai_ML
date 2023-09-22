import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
data = pd.read_csv("D:/WineQT.csv")

# print(data.head())
# print(data.shape)
# print(data.describe())
# print(data.info())
# print(data["quality"].unique())



# x= np.array([4, 5, 6, 10, 30, 12])
# y= np.array([2, 3, 4, 5,30 ,14])
# plt.plot(x, y)
# plt.plot(x, y, linestyle = "dotted")
# x= np.array([5, 15, 30])
# y= np.array([5, 10, 30])
# plt.bar(x, y)
# plt.scatter(x, y)

# z = np.array([25, 25, 35, 15])
# plt.pie(z)

#
# x = np.array([25, 25, 35, 15])
#
# sns.distplot(x)
# plt.show()
#

# flights_data = sns.load_dataset("flights")
# print(flights_data)
# may_flights = flights_data.query("month == 'May'")
# print(may_flights)
# sns.lineplot(data=may_flights, x="year", y="passengers" )
# plt.show()
# df  = sns.load_dataset("penguins")
# print(df.head())
#
# sns.barplot(data=df,x="island",y="body_mass_g")
# plt.show()

# x = np.array([1,2,3])
# y = np.array([6,7,8])
#
# fig = px.bar(x, y)

df = px.data.tips()

# print(df.head())

fig = px.pie(df, values="tip", names= 'day')
fig.show()