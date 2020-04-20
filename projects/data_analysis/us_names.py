import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('D:/Cloud/Nastya/IT/python/NationalNames.csv')
millenial = df.loc[df['Year']>=1980].loc[df['Year']<=1994]
millenial_man = millenial.loc[millenial['Gender']=='M']
years = [year for year, millenial in millenial.groupby('Year')]

mill_name = pd.DataFrame() # make new file
for year in years:
	# mill_name = pd.concat([mill_name, millenial_man.loc[millenial['Year']==year][:5][['Year','Name','Count']]])
	mill_name = pd.concat([mill_name, millenial_man.loc[millenial['Year']==year].nlargest(3, 'Count')[['Year','Name','Count']]])

names = [name for name, millenial in mill_name.groupby('Name')]
print(names)

# mill_fig = px.area(mill_name.loc[mill_name['Name']=='Michael'], x='Year', y = 'Count', title='Michael')
# mill_fig.show()


fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[0, 2, 3, 5], fill='tozeroy')) # fill down to xaxis


# print(mill_name.loc[mill_name['Name']=='Michael'].sum())
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=mill_name['Year'], y=mill_name['Count'],
#                     mode='lines+markers', name=1))
# # fig.add_trace(go.Scatter(x=usa_deaths_more_w_ny['Province_State'], y=usa_deaths_more_w_ny['Active'],
# #                     mode='lines+markers', name='Active'))
# # fig.add_trace(go.Scatter(x=usa_deaths_more_w_ny['Province_State'], y=usa_deaths_more_w_ny['Recovered'],
# #                     mode='lines+markers', name='Recovered'))
# fig.add_trace(go.Scatter(x=mill_name['Year'], y=mill_name['Count'],
#                     mode='lines+markers', name=2))
# fig.show()


print(mill_name.head(30))
