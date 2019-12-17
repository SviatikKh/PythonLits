import requests
import pyowm
import json

# Прогноз погоди звичайний

# city = input('Vvedit Vashe misto latynyceju: ')

# my_id = 'http://api.openweathermap.org/data/2.5/weather?appid=a1e4c3dee5310ded3052b1dd6d802bee&q='
# url = my_id + city
# json_data = requests.get(url).json()
# format = json_data["main"]
# print(format)

#Через бібліотеку pyowm

# city = input('Введіть Ваше місто латиницею: ')
# owm = pyowm.OWM('a1e4c3dee5310ded3052b1dd6d802bee')
# observation = owm.weather_at_place(city)
# w = observation.get_weather()
# print(w)
# wind = w.get_wind()
# humidity = w.get_humidity()
# temp = w.get_temperature('celsius')
# print('Вітер', wind)
# print('Вологість', humidity)
# print('Температура', temp)


#Погода на Марсі

# with open('C:/Users/PC/Desktop/Lits/L14/mars_weather.json', 'r') as file_json:
#     weather = json.load(file_json)
#     print(weather)
#     print(weather['211']['Season'])
#     print(isinstance(weather, dict))
