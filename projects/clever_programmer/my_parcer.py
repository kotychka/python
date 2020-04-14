import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XpMwXs1S_IU')
soup = BeautifulSoup(page.content, 'html.parser')

# Take div with all needed data
week = soup.find(id='seven-day-forecast-list')
items = week.find_all(class_='tombstone-container')

# Take data to variables
period_names = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
temp = [item.find(class_='temp').get_text() for item in items]

# print(period_names)
# print(short_desc)
# print(temp)

weather_stuff = pd.DataFrame(
	{ 
		'period': period_names,
		'short-descriptions': short_desc,
		'temperatures': temp,
	})	

print(weather_stuff)

weather_stuff.to_csv('weather.csv')