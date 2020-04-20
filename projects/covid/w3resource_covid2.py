# import pandas as pd
# covid_data = pd.read_csv('../../COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/04-17-2020.csv')
# # covid_data = pd.read_csv('././pandas/04-17-2020.csv')
# # covid_data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/04-17-2020.csv')
# print(covid_data.head())

import pandas as pd
import matplotlib.pyplot as plt
covid_data = pd.read_csv('D:/Cloud/Nastya/IT/python/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/04-17-2020.csv')
# covid_data2 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-18-2020.csv')
ex1 = covid_data.head() # 1ex.
ex2 = covid_data.groupby('Country_Region').sum() # 2ex - the latest number of confirmed, deaths, recovered and active cases Country wise
# ex3 = covid_data.groupby(['Country_Region', 'Province_State']).sum()[['Deaths','Recovered']] # 3ex - the latest number of confirmed deaths and recovered people Country/Region - Province/State wise
# ex4 = covid_data.loc[covid_data['Country_Region']=='China'].groupby(['Province_State']).sum()[['Confirmed','Deaths','Recovered']] # 4ex - the Chinese province wise cases of confirmed, deaths and recovered cases
# ex5 = covid_data.groupby('Country_Region').sum()['Deaths'] # 5ex - the latest country wise deaths cases
# ex6 = covid_data.loc[covid_data['Recovered']==0].groupby(['Country_Region']) #6ex - list countries with no cases recovered
# ex7 = covid_data.loc[(covid_data['Deaths'] == covid_data['Confirmed']) & (covid_data['Confirmed'] > 0)] # 7ex - list countries with all cases died
# ex8 = covid_data.loc[(covid_data['Recovered'] == covid_data['Confirmed']) & (covid_data['Confirmed'] > 0)] # 8ex - list countries with all cases recovered
# ex9 = covid_data.groupby(['Country_Region']).sum().sort_values(['Confirmed'], ascending=False)[['Confirmed','Deaths','Recovered']].head(10) # 9ex - get the top 10 countries data (Last Update, Country/Region, Confirmed, Deaths, Recovered)
#10ex - create a plot (lines) of total deaths, confirmed, recovered and active cases Country wise where deaths greater than 150
table = ex2[['Confirmed','Deaths','Recovered','Active']]
countr = table.loc[table['Deaths'] > 650]
countries = [country for country,countr in countr['Confirmed'].items()] # array of cities for graph
plt.figure(figsize=(20,10))
plt.plot(countries, countr['Confirmed'], color='skyblue', linewidth=2, label="Confirmed")
plt.plot(countries, countr['Deaths'], color='red', linewidth=2, label="Deaths")
plt.plot(countries, countr['Recovered'], color='green', linewidth=2, label="Recovered")
plt.plot(countries, countr['Active'],  color='yellow', linewidth=2, label="Active")
plt.legend()
plt.grid()
plt.xticks(countries, rotation='vertical', size=14)
plt.show()
