import pandas as pd
#
# df = pd.DataFrame(
#     {
#         "column1": [1, 2, 3],
#         "column2": [4, 5, 6],
#         "column3": [7, 8, 9]
#     },
#     index=[10, 20, 30]
#
# )
# print(df)

# df = pd.DataFrame(
#     {
#         "column1": [1, 2],
#         "column2": [4, 5],
#     },
#     index=[10, 20]
#
# )
# print(df)
#
# y = pd.DataFrame(
#     [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ],
#     index=[1, 2, 3],
#     columns=['column1', 'column2', 'column3']
#
# )
# print(y)
#
# z = pd.concat([df, y])
# print(z)
#
#
# v = pd.melt(df)
# print(v)
# z = pd.concat([df, y],axis=1)
# print(z)

# data = pd.DataFrame(
#     {
#         "col1": [2, 3, 4, 5],
#         "col2": [7, 8, 9, 6],
#         "col3": [9, 5, 4, 7],
#         "col4": [8, 6, 7, 3]
#     },
#     index=pd.MultiIndex.from_tuples(
#         [
#             ("d", 1),
#             ("d", 2),
#             ("d", 3),
#             ("b", 4)
#         ],
#         names=["class", "id"]
#     )
# )
# print(data)


data = pd.read_csv("D:/data.csv")
print(data)


# ------------------ Exploratory Data Analysis ---------------------------

# print(data.head(4))
# print(data.tail(4))

#
# print(data.info())
# print(data.describe())

# print(data["JobTitle"].unique())
# print(data["Agency"].unique())

# print(data["Agency"].value_counts())
#
# print(data["Year"].value_counts())

# data.drop(columns=["Notes"], inplace=True)
# print(data.head())

