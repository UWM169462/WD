import pandas as pd
import numpy as np

df=pd.read_excel("imiona.xlsx")
# print(df) #16416

# for x in range(len(df)):
#     if df.at[x, "Liczba"] > 1000:
#         print(df.loc[x])

# for x in range(len(df)):
#     if df.at[x, "Imie"] == "MICHAŁ":
#         print(df.loc[x])

# # print(df.groupby('Rok')['Liczba'].sum())
#?????? print(df.Liczba.sum)

# df_filtered = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]
# # print(df_filtered.groupby('Rok')['Liczba'].sum())
# df_filtered.sum
# print(df.groupby(['Plec','Rok'])['Liczba'].sum())


