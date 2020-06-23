#%%
import pandas as pd
import numpy as np
#%%
df = pd.read_csv("Semana 2/Datos/daily_weather.csv")

#%%
df.isnull().sum()

#%%
df.dropna(axis=0,inplace=True)

#%%
df['air_pressure_9am'].loc[(df['air_pressure_9am']>=911.736) & (df['air_pressure_9am']<=914.67)].count()

#%%
df = pd.read_csv("Semana 2/Datos/daily_weather.csv")
df.replace(np.nan,df.min(),inplace=True)

#%%
df['air_temp_9am'].loc[df['air_temp_9am']<42.292].count()

#%%
df = pd.read_csv("Semana 2/Datos/daily_weather.csv")
df.isnull().sum()

#%%
