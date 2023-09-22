import pandas as pd
import glob
#
#
# # 1- read mexico-real-estate-1.csv into df
#
# df = pd.read_csv("D:/data/mexico-real-estate-1.csv",encoding='latin-1')
# print(df.head())
#
# # 2- get only the apartment that locates in mexico city "Distrito Federal" that costs less than 100,000
# # -------------------------------------The data is incomplete, some columns do not exist ----------------------------------------------
# # df = df[df["state"] == "Distrito Federal"] and df["price_usd"] < 100000
# # print(df)
#
#
# # 3- create seperate "lat" and "lon" columns as done before
#
# df[['lat', 'lon']] = df['lat-lon'].str.split(',', expand=True).astype(float)
#
# print(df)


# ---------------------------This part of the test I was able to solve and the rest I don't understand and I can't solve-----------------------------------------
