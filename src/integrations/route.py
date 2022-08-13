"""
Integration for extracting route information.
This implementation was based on https://openrouteservice.org/dev/#/home
"""
import logging
import requests
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

API_TOKEN = os.environ['ROUTE_API_TOKEN']
BASE_URL = os.environ['ROUTE_API_BASE_URL']
VEHICLE = os.environ['ROUTE_API_VEHICLE']

def get_duration(origin_geo: list, destiny_geo: list):
    """
    Gets route duration in seconds

    Parameters
    ----------
    origin_geo: list
        longitude and latitude of origin city. Ex: [-46.26875541668693,-23.973708062833566]
    destiny_geo: list
        longitude and latitude of destiny city. Ex: [-46.26875541668693,-23.973708062833566]
    
    Returns
    -------
    condition
        The current weather condition from city_id 
    """
    logger.info(f'Loading route duration from {str(origin_geo)} to {str(destiny_geo)}')
    url = f"{BASE_URL}{origin_geo[1]}%2C{origin_geo[0]}%3A{destiny_geo[1]}%2C{destiny_geo[0]}/json?routeRepresentation=summaryOnly&computeTravelTimeFor=all&traffic=true&travelMode={VEHICLE}&vehicleCommercial=true&key={API_TOKEN}"
    logger.info(f'URL for route: {url}')
    try:
        headers = {'accept': '*/*'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()['routes'][0]['summary']['travelTimeInSeconds']
    except requests.HTTPError as http_err:
        logger.error(f'HTTP error occurred: {http_err}')
    except Exception as err:
        logger.error(f'Error occurred: {err}')
