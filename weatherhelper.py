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

class WeatherInfoResult(object):
    def __init__(self, city, success, json_data=None):
        self.success = success
        self.city = city
        if success:
            # transform data
            # request 1: Set the [weather] field, as [heavy rain  /   rain /  SunnyCloud / snow ]
            weather = json_data['weather'][0]
            self.main = weather['main']
            self.temp = json_data['main']['temp']
            # request 2: 
            

class WeatherFetcher(object):

    @staticmethod 
    def getCurrentSydneyWeather():
        logger = logging.getLogger('root')
        logger.debug("WeatherFetcher.getCurrentSydneyWeather")
        city = "sydney"
        appid = "5f663fbed54c152530cd4f6fdab3c221"
        query = {'q': city, 'appid': appid}
        # extract data
        response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=query)

        if (response.status_code == 200):
            logger.debug("WeatherFetcher.getCurrentSydneyWeather return successfully")
            #logger.debug(response.json())
            return WeatherInfoResult(city, True, response.json())
        else:
            logger.debug(f"WeatherFetcher.getCurrentSydneyWeather return error code: {response.status_code}")
            return WeatherInfoResult(city, False)
            
        
        
    