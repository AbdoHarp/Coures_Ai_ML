import pandas as pd

# Import the CSV file into a DataFrame
df = pd.read_csv('D:/data/brasil-real-estate-1.csv',  encoding='latin-1')
# print(df.head())
#
# # Drop rows with NaN values
# dro = df.dropna()
# print(dro)
#
# # Task 3: use "lat-lon" columns to create two seperate columns in df "lat", "lon". make sure that the datatype will be float
# # #
# df[['lat', 'lon']] = df['lat-lon'].str.split(',', expand=True).astype(float)
# print(df)
# #
# # # Task 4: Transform "price_USD" so that all values be floating points instead of strigns
# #
# df['price_USD'] = df['price_USD'].str.replace(',', '').astype(float)
# print(df)
# #
# # # Task 5: drop "lat-lon" columns
# #
# df = df.drop('lat-lon', axis=1)
# print(df)
#
#
#
# Import the CSV file into a DataFrame
df2 = pd.read_csv('D:/data/brasil-real-estate-2.csv',encoding='latin-1')
print(df2.head())
# # Task 7: use "price_berl" to create new columns named "price_usd" by dividing the value by 3.19
#
# df2['price_usd'] = df2['price_brl'] / 3.19
# print(df2)
#
# # Task 8: drop "price_brl" from columns, as well as any rows that have Nan values
#
# df2 = df2.dropna(subset=['price_brl'])
# df2 = df2.drop('price_brl', axis=1)
# print(df2)
#
# # Task 9: concatenate df and df2 into new dataframe named df_new
#
df_new = pd.concat([df, df2], ignore_index=True)
# print(df_new)
#
# # Task 10: use describe method to create dataframe summary_stats for "area_m2" and "price_usd" columns
#
summary_stats = df_new[['area_m2', 'price_usd']].describe()
# print(summary_stats)

# # Task 12: create new dataframe named df_south that contains all homes from df in South region
#
df_south = df[df['region'] == 'South']
print(df_south)
#
#
# # Task 13: use value_counts method to ctreate a series home_by_state that contains the number of properties in df_south
# # Create a Series home_by_state with the number of properties in df_south
home_by_state = df_south['state'].value_counts()
print(home_by_state)


