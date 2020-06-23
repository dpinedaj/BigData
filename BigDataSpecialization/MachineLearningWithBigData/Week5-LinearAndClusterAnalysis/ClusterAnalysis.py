#%%
import pandas as pd

#%%
df= pd.read_csv("minute_weather.csv")

#%%
df.info()

#%%
df.isnull().sum()

#%%
df.describe().transpose()


#%%
df.isnull().sum()
#%%
df.dropna(axis=0,inplace=True)


#%%
df[(df.rain_accumulation==0)].count()

#%%
1577452/10


#%%
