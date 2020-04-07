import pyowm
from colorama import init
init()
from colorama import Fore, Back, Style

owm = pyowm.OWM('385572756a72f12ab127c4c8bfdaeb79')  # You MUST provide a valid API key

print(Fore.BLACK)
print(Back.GREEN)

city = input("Type the city: ")
observation = owm.weather_at_place(city)
w = observation.get_weather()
temp = w.get_temperature('celsius')['temp']
wind = w.get_wind()['speed']
humidity = w.get_humidity()

print(Back.CYAN)
print('The temperature in ' + city + ' ' + str(temp) + '. The wind speed is ' + str(wind) + 'm/s. Humidity is ' + str(humidity) + '%')

input()