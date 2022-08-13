"""
Integration for extracting weather information from cities.
This implementation was based on https://openweathermap.org/api
"""
import datetime
import logging
import requests
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

API_TOKEN = os.environ['WEATHER_API_TOKEN']
UNITS = os.environ['WEATHER_API_UNITS']
BASE_URL = os.environ['WEATHER_API_BASE_URL']

def get_current_conditions(city_id: str):
    """
    Get the current weather condition for city_id from OpenWeatherMap service

    Parameters
    ----------
    city_id: str
        The city id based on openweathermap relation
    
    Returns
    -------
    condition
        the current weather condition from city_id 
    """
    current_time = datetime.datetime.now().time()
    logger.info(f'Loading current weather conditions for city {city_id} at {current_time}')
    url = BASE_URL + '?id=' + city_id + '&units=' + UNITS + '&appid=' + API_TOKEN 
    logger.info(f'url = {url}')
    try:
        logger.info('Running HTTP request...')
        response = requests.get(url)
        logger.info('Request completed')
        response.raise_for_status()
        logger.info(f'Response = {response.json()}')
        return response.json()
    except requests.HTTPError as http_err:
        logger.error(f'HTTP error occurred: {http_err}')
    except Exception as err:
        logger.error(f'Error occurred: {err}')
