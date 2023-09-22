import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("D:/data/diabetes.csv")
# print(df.head())
# print(df.shape)
# print(df.info)
# print(df.isnull().any())

fig ,axs = plt.subplots(9,1, dpi=65, figsize=(7,17))
i=0
for col in df.columns:
    axs[i].boxplot(df[col],vert= False)
    axs[i].set_ylabel(col)
    i+=1
plt.show()