import pandas as pd
import plotly.graph_objects as go
import re
import numpy as np

df = pd.read_csv('D:/Cloud/Nastya/IT/python/Neighborhood_Zri_AllHomesPlusMultifamily.csv') # reading data
city = 'San Diego'
df_city = df.loc[df['City']==city] # choosing city

## filling missing data
# geting the first column with floats
col_numb = 0
for col in df_city.dtypes:
    if col != 'float64': 
        col_numb +=1
    else: break
# filling NaN with mean
df_city[df_city.columns[col_numb:]] = df_city[df_city.columns[col_numb:]].interpolate(axis=1) 

## geting the list of years that is in the data
# taking all columns and slicing it to get years
col_names=''
for col in df_city.columns:
    if col[0]=='2':
        col_names += col[:4]+','
    else: continue
# intilize a null list 
unique_col_names = []
# traverse for all elements 
for x in col_names.split(',')[:-1]: 
    # check if exists in unique_list or not 
    if x not in unique_col_names: 
        unique_col_names.append(x)

## counting number of columns in df
col_quant = -1
for col in df_city.columns:
    col_quant += 1

## add new data
# create new df
df_miami_new = df_city.copy()
# add columns with yearly changes in prices in comparison with first data
col_quant2 = col_quant # variable to know how many columns after adding
for col in unique_col_names[1:-1]:
    df_miami_new[col] = (df_city[col+'-12'] - df_city.iloc[:,col_numb])/df_city.iloc[:,col_numb]*100
    col_quant2 += 1
# add new columns with monthly changes
col_quant3 = col_quant2 # variable to know how many columns after adding
for col in df_city.columns[col_numb:]:
    df_miami_new[col+' changes'] = (df_city[col] - df_city.iloc[:,col_numb])/df_city.iloc[:,col_numb]*100
    col_quant3 += 1

### dynamic for some years
## getting year for slicing data
# print('Enter the year that you want to see. If you want to see dynamic since 2010 to 2020 enter: "2"')
# year = input()
year = '2'
mean = df_city.iloc[:,col_quant].mean() # finding point to split graphs

### graph with % of monthly changing in prices
## expensive regions
# prepearing data
df_miami_slice = df_miami_new.loc[df_city.iloc[:,col_quant]>mean] # slicing needed data
df_miami_year = df_miami_slice.set_index('RegionName').transpose().reset_index()[col_quant2+1:] # transposing columns into rows
# draw lines
fig = go.Figure()
for region in df_miami_slice['RegionName'].unique():
  fig.add_trace(go.Scatter(y=df_miami_year[region], x=df_miami_year['index'], mode='lines+markers', name=region))
fig.update_layout(title={'text': "The dynamic of monthly changing average prices of 1br in "+city+" in expensive regions"}, width=1050, height=600)
fig.show()

# ## cheap regions
# # prepearing data
df_miami_slice = df_miami_new.loc[df_city.iloc[:,col_quant]<=mean] # slicing needed data
df_miami_year = df_miami_slice.set_index('RegionName').transpose().reset_index()[col_quant2+1:] # transposing columns into rows
# draw lines    
fig = go.Figure()
for region in df_miami_slice['RegionName'].unique():
  fig.add_trace(go.Scatter(y=df_miami_year[region], x=df_miami_year['index'], mode='lines+markers', name=region))
fig.update_layout(title={'text': "The dynamic of monthly changing average prices of 1br in "+city+" in cheap regions"}, width=1050, height=600)
fig.show()

# ### graph with % of yearly changing in prices
# ## expensive regions
# # prepearing data
# df_miami_slice = df_miami_new.loc[df_city.iloc[:,col_quant]>mean] # slicing needed data
# df_miami_year = df_miami_slice.set_index('RegionName').transpose().reset_index()[col_quant+1:col_quant2+1] # transposing columns into rows
# # draw lines
# fig = go.Figure()
# for region in df_miami_slice['RegionName'].unique():
#   fig.add_trace(go.Scatter(y=df_miami_year[region], x=df_miami_year['index'], mode='lines+markers', name=region))
# fig.update_layout(title={'text': "The dynamic of yearly changing average prices of 1br in "+city+" in expensive regions"}, width=1000, height=600)
# fig.show()

# ## cheap regions
# # prepearing data
# df_miami_slice = df_miami_new.loc[df_city.iloc[:,col_quant]<=mean] # slicing needed data
# df_miami_year = df_miami_slice.set_index('RegionName').transpose().reset_index()[col_quant+1:col_quant2+1] # transposing columns into rows
# # draw lines
# fig = go.Figure()
# for region in df_miami_slice['RegionName'].unique():
#   fig.add_trace(go.Scatter(y=df_miami_year[region], x=df_miami_year['index'], mode='lines+markers', name=region))
# fig.update_layout(title={'text': "The dynamic of yearly changing average prices of 1br in "+city+" in cheap regions"}, width=1000, height=600)
# fig.show()

### graph with simple dynamic
## expensive regions
# prepearing data
df_miami_slice = df_city.loc[df_city.iloc[:,col_quant]>mean] # slicing needed data
df_miami_year = df_miami_slice.set_index('RegionName').transpose().reset_index() # transposing columns into rows
df_miami_year = df_miami_year.loc[df_miami_year['index'].str.contains(year)] # cutting data for certain year
# draw lines    
fig = go.Figure()
for region in df_miami_slice['RegionName'].unique():
    fig.add_trace(go.Scatter(y=df_miami_year[region], x=df_miami_year['index'], mode='lines+markers', name=region))
fig.update_layout(title={'text': "The dynamic of average prices of 1br in "+city+" in expensive regions"}, width=1000, height=600)
fig.show()

## cheap regions
# prepearing data
df_miami_slice = df_city.loc[df_city.iloc[:,col_quant]<=mean] # slicing needed data
df_miami_year = df_miami_slice.set_index('RegionName').transpose().reset_index() # transposing columns into rows
df_miami_year = df_miami_year.loc[df_miami_year['index'].str.contains(year)] # cutting data for certain year
# draw lines    
fig = go.Figure()
for region in df_miami_slice['RegionName'].unique():
    fig.add_trace(go.Scatter(y=df_miami_year[region], x=df_miami_year['index'], mode='lines+markers', name=region))
fig.update_layout(title={'text': "The dynamic of average prices of 1br in "+city+" in cheap regions"}, width=1000, height=600)
fig.show()