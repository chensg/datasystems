"""
This class is designed to fetch weather data from below API
Website account information:
https://home.openweathermap.org/
username: 41091datasystems@gmail.com
password: qX_7X6L9p4x9ps-
API information:
API keys: 5f663fbed54c152530cd4f6fdab3c221
api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
"""

import logging
import json
import requests
from dbhelper import DatabaseHelper

class WeatherInfoResult(object):
    def __init__(self, city, success, json_data=None):
        self.success = success
        self.city = city
        self.json_data = json_data
        self.db = DatabaseHelper.getInstance()
    
    def transform(self):
        # transform data
        # request 1: Set the [weather] field, as [heavy rain  /   rain /  SunnyCloud / snow ]
        self.weather = self.json_data['weather'][0]['main'].lower()
        # request 2: Compute  the [temperature] field by using lowest or highest temperature 
        # Set the [temperature] to [High/ Low /Normal ] 
        # by setting  
        #  [High :  (daily highest temperature)  > 35 degrees] 
        #  [Low : (daily lowest temperature)    <  10 degrees ]
        #  [Normal    10 <temperature <35 ]
        temperature_highest = float(self.json_data['main']['temp_max'])
        temperature_lowest = float(self.json_data['main']['temp_min'])
        if temperature_highest > 35:
            self.temperature = "High"
        elif temperature_lowest < 10:
            self.temperature = "Low"
        else:
            self.temperature = "Normal"

    def load(self):
        # example only, update the last record in fact table
        logger = logging.getLogger('root')
        logger.debug(self.weather)
        self.db.updateWeatherInfo(self)

class WeatherFetcher(object):

    @staticmethod 
    def getCurrentSydneyWeather():
        logger = logging.getLogger('root')
        logger.debug("WeatherFetcher.getCurrentSydneyWeather")
        city = "sydney"
        appid = "5f663fbed54c152530cd4f6fdab3c221"
        query = {'q': city, 'appid': appid, 'units': 'metric'}
        # extract data
        response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=query)

        if (response.status_code == 200):
            logger.debug("WeatherFetcher.getCurrentSydneyWeather return successfully")
            #logger.debug(response.json())
            return WeatherInfoResult(city, True, response.json())
        else:
            logger.debug(f"WeatherFetcher.getCurrentSydneyWeather return error code: {response.status_code}")
            return WeatherInfoResult(city, False)