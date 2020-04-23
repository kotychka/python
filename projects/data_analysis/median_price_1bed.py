import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('D:/Cloud/Nastya/IT/python/median_price.csv') # reading data
df.loc[df['State']=='FL'].head(40)
df.loc[df['City'].str.contains('Miami')].head(40)
df_miami = df.loc[df['City']=='Miami']

df_miami_ind = df_miami.set_index('RegionName')
df_miami_transp = df_miami_ind[df_miami_ind.columns[6:]].transpose()

## Lines by years
# adding new columns with yearly mean
for year in list(map(str,range(2010,2017))):
    df_miami[year] = df_miami.filter(like=year, axis=1).mean(axis=1)
df_miami_new = df_miami.set_index('RegionName').transpose().reset_index().iloc[-7:] #  transposing columns into rows
# draw lines

fig = make_subplots(1,2)
for region in df_miami['RegionName']:
	fig.add_trace(go.Scatter(y=df_miami_new[region], x=df_miami_new['index'], mode='lines+markers', name=region), row = 1, col = 1)

df_miami_new2 = df_miami.set_index('RegionName').transpose().reset_index().iloc[5:] #  transposing columns into rows
for region in df_miami['RegionName']:
	fig.add_trace(go.Scatter(y=df_miami_new2[region], x=df_miami_new2['index'], mode='lines+markers', name=region),row = 1, col = 2)
fig.show()