import pandas as pd

df = pd.read_csv("expenses.csv")
#%%
df.info()
#%%
df.drop_duplicates(inplace=True)
#%%
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df.info()
#%%
df['date'] = df['date'].dt.strftime('%d/%m/%Y')
print(df.to_string())
#%%



