import pandas as pd

url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'

dfs = pd.read_html(url)

df_bancos = dfs[0]

#print(type(dfs))

#print(len(dfs))

#print(df_bancos.shape)

#print(df_bancos.dtypes)

print(df_bancos.head())
