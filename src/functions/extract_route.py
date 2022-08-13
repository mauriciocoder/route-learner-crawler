# import ptvsd
# ptvsd.enable_attach(address=('0.0.0.0', 5890), redirect_output=True)
# ptvsd.wait_for_attach()
import datetime
import logging
import os
from src.integrations import route, weather
from src.models.route import Route

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

CITY_IDS = os.environ['CITY_IDS'].split(',')

# Origin and Destiny Long/Lat
ORIGIN_GEO = [float(n) for n in os.environ['GEO_ORIGIN'].split(',')]
DESTINY_GEO = [float(n) for n in os.environ['GEO_DESTINY'].split(',')]

def run(event, context):
    logger.info("Extracting route...")
    r = Route(ORIGIN_GEO, DESTINY_GEO)
    for city_id in CITY_IDS:
        r.add_weather_condition(weather.get_current_conditions(city_id))
    r.duration = route.get_duration(ORIGIN_GEO, DESTINY_GEO)
    logger.info("Route extracted")
    r.save()
    logger.info(f"Route extracted at {datetime.datetime.now().time()}")
    
    