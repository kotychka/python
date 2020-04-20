import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('D:/Cloud/Nastya/IT/python/NationalNames.csv') # reading data

### millenials
millenial = df.loc[df['Year']>=1980].loc[df['Year']<=1994] # choosing millenial yers
millenial_man = millenial.loc[millenial['Gender']=='M'] # choosing male data
millenial_fem = millenial.loc[millenial['Gender']=='F'] # choosing female data
mill_years = [year for year, millenial in millenial.groupby('Year')] # writing years

## choosing the most popular male names by years
mill_name = pd.DataFrame() # make new df to add there data
for year in mill_years:
	mill_name = pd.concat([mill_name, millenial_man.loc[millenial['Year']==year].nlargest(4, 'Count')[['Year','Name','Count']]]) # 4 most popular names

## draw lines with popular male names during millenial years
fig = go.Figure()
names = [name for name, millenial in mill_name.groupby('Name')] # writing the most popular male names
for name in names:
	df_name = millenial_man.loc[millenial_man['Name']==name]
	fig.add_trace(go.Scatter(x=df_name['Year'], y=df_name['Count'], mode='lines+markers', name=name))
fig.update_layout(title={'text': "The most popular male names of Millenials"})
fig.show()

## choosing the most popular female names by years
mill_name = pd.DataFrame() # make new df to add there data
for year in mill_years:
	mill_name = pd.concat([mill_name, millenial_fem.loc[millenial['Year']==year].nlargest(3, 'Count')[['Year','Name','Count']]]) # 4 most popular names

## draw lines with popular male names during millenial years
fig = go.Figure()
names = [name for name, millenial in mill_name.groupby('Name')] # writing the most popular male names
for name in names:
	df_name = millenial_fem.loc[millenial_fem['Name']==name]
	fig.add_trace(go.Scatter(x=df_name['Year'], y=df_name['Count'], mode='lines+markers', name=name))
fig.update_layout(title={'text': "The most popular female names of Millenials"})
fig.show()


### gen z
gen_z = df.loc[df['Year']>=1995].loc[df['Year']<=2012] # choosing gen z yers
gen_z_man = gen_z.loc[gen_z['Gender']=='M'] # choosing male data
gen_z_fem = gen_z.loc[gen_z['Gender']=='F'] # choosing female data
gen_z_years = [year for year, gen_z in gen_z.groupby('Year')] # writing years

## choosing the most popular male names by years
gen_z_name = pd.DataFrame() # make new df to add there data
for year in gen_z_years:
	gen_z_name = pd.concat([gen_z_name, gen_z_man.loc[gen_z['Year']==year].nlargest(3, 'Count')[['Year','Name','Count']]]) # 4 most popular names

## draw lines with popular male names during gen z years
fig = go.Figure()
names = [name for name, gen_z in gen_z_name.groupby('Name')] # writing the most popular male names
for name in names:
	df_name = gen_z_man.loc[gen_z_man['Name']==name]
	fig.add_trace(go.Scatter(x=df_name['Year'], y=df_name['Count'], mode='lines+markers', name=name))
fig.update_layout(title={'text': "The most popular male names of Gen Z"})
fig.show()

## choosing the most popular female names by years
gen_z_name = pd.DataFrame() # make new df to add there data
for year in gen_z_years:
	gen_z_name = pd.concat([gen_z_name, gen_z_fem.loc[gen_z['Year']==year].nlargest(2, 'Count')[['Year','Name','Count']]]) # 4 most popular names

## draw lines with popular male names during gen z years
fig = go.Figure()
names = [name for name, gen_z in gen_z_name.groupby('Name')] # writing the most popular male names
for name in names:
	df_name = gen_z_fem.loc[gen_z_fem['Name']==name]
	fig.add_trace(go.Scatter(x=df_name['Year'], y=df_name['Count'], mode='lines+markers', name=name))
fig.update_layout(title={'text': "The most popular female names of Gen Z"})
fig.show()
