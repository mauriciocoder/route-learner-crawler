from asyncio.log import logger
from sqlalchemy import Column, Integer, Numeric, Boolean
from src.models import Base
import pytz
import datetime
import holidays

class Route(Base):
    origin_latitude = Column(Numeric)
    origin_longitude = Column(Numeric)
    destiny_latitude = Column(Numeric)
    destiny_longitude = Column(Numeric)

    week_day = Column(Integer) # Monday = 0, ... Sunday = 6
    day_of_month = Column(Integer)
    month = Column(Integer)
    day_before_holiday = Column(Boolean)
    holiday = Column(Boolean)
    day_after_holiday = Column(Boolean)

    p1_weather_id = Column(Integer)
    p1_weather_description_id = Column(Integer)
    p1_city_id = Column(Integer)
    p1_temperature = Column(Numeric)
    p1_feels_like = Column(Numeric)
    p1_pressure = Column(Integer)
    p1_humidity = Column(Integer)
    p1_visibility = Column(Integer)
    p1_wind_degree = Column(Integer)
    p1_wind_speed = Column(Numeric)

    p2_weather_id = Column(Integer)
    p2_weather_description_id = Column(Integer)
    p2_city_id = Column(Integer)
    p2_temperature = Column(Numeric)
    p2_feels_like = Column(Numeric)
    p2_pressure = Column(Integer)
    p2_humidity = Column(Integer)
    p2_visibility = Column(Integer)
    p2_wind_degree = Column(Integer)
    p2_wind_speed = Column(Numeric)

    p3_weather_id = Column(Integer)
    p3_weather_description_id = Column(Integer)
    p3_city_id = Column(Integer)
    p3_temperature = Column(Numeric)
    p3_feels_like = Column(Numeric)
    p3_pressure = Column(Integer)
    p3_humidity = Column(Integer)
    p3_visibility = Column(Integer)
    p3_wind_degree = Column(Integer)
    p3_wind_speed = Column(Numeric)

    p4_weather_id = Column(Integer)
    p4_weather_description_id = Column(Integer)
    p4_city_id = Column(Integer)
    p4_temperature = Column(Numeric)
    p4_feels_like = Column(Numeric)
    p4_pressure = Column(Integer)
    p4_humidity = Column(Integer)
    p4_visibility = Column(Integer)
    p4_wind_degree = Column(Integer)
    p4_wind_speed = Column(Numeric)

    duration = Column(Integer)

    def __init__(self, origin_geo, destiny_geo):
        self.origin_latitude = origin_geo[1]
        self.origin_longitude = origin_geo[0]
        self.destiny_latitude = destiny_geo[1]
        self.destiny_longitude = destiny_geo[0]

        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        brt_now = utc_now.astimezone(pytz.timezone("America/Sao_Paulo"))
        print(brt_now)

        self.week_day = brt_now.weekday()
        self.day_of_month = brt_now.day
        self.month = brt_now.month
        year = brt_now.year
        print(f'week_day = {self.week_day} | day_of_month = {self.day_of_month} | month = {self.month} | year = {year}')

        # TODO check if it has all regional holidays
        hs = holidays.Brazil(years=year, subdiv='SP')
        for h in hs.items():
            self.holiday = (brt_now.date() == h[0])
            
            day_before_holiday = h[0] - datetime.timedelta(days=1)
            self.day_before_holiday = (brt_now.date() == day_before_holiday)

            day_after_holiday = h[0] + datetime.timedelta(days=1)
            self.day_after_holiday = (brt_now.date() == day_after_holiday)

    def add_weather_condition(self, condition: dict):
        """
        Add a weather condition to one of the four cities mapped.
        It incrementaly add the weather to whatever city that is 
        still not covered, from first to last

        Parameters
        ----------
        condition: dict
            The weather condition taken from integration
         
        """
        try:
            sys_id = condition['sys']['id']
        except:
            sys_id = 0
            logger.warn('Unable to obtain sys.id, default to zero')
        # TODO: Refactor the conditions below
        if self.p1_weather_id is None:
            self.p1_weather_id = sys_id
            self.p1_weather_description_id = condition['weather'][0]['id']
            self.p1_city_id = condition['id']
            self.p1_temperature = condition['main']['temp']
            self.p1_feels_like = condition['main']['feels_like']
            self.p1_pressure = condition['main']['pressure']
            self.p1_humidity = condition['main']['humidity']
            self.p1_visibility = condition['main']['humidity']
            self.p1_wind_degree = condition['wind']['deg']
            self.p1_wind_speed = condition['wind']['speed']
        elif self.p2_weather_id is None:
            self.p2_weather_id = sys_id
            self.p2_weather_description_id = condition['weather'][0]['id']
            self.p2_city_id = condition['id']
            self.p2_temperature = condition['main']['temp']
            self.p2_feels_like = condition['main']['feels_like']
            self.p2_pressure = condition['main']['pressure']
            self.p2_humidity = condition['main']['humidity']
            self.p2_visibility = condition['main']['humidity']
            self.p2_wind_degree = condition['wind']['deg']
            self.p2_wind_speed = condition['wind']['speed']
        elif self.p3_weather_id is None:
            self.p3_weather_id = sys_id
            self.p3_weather_description_id = condition['weather'][0]['id']
            self.p3_city_id = condition['id']
            self.p3_temperature = condition['main']['temp']
            self.p3_feels_like = condition['main']['feels_like']
            self.p3_pressure = condition['main']['pressure']
            self.p3_humidity = condition['main']['humidity']
            self.p3_visibility = condition['main']['humidity']
            self.p3_wind_degree = condition['wind']['deg']
            self.p3_wind_speed = condition['wind']['speed']
        elif self.p4_weather_id is None:
            self.p4_weather_id = sys_id
            self.p4_weather_description_id = condition['weather'][0]['id']
            self.p4_city_id = condition['id']
            self.p4_temperature = condition['main']['temp']
            self.p4_feels_like = condition['main']['feels_like']
            self.p4_pressure = condition['main']['pressure']
            self.p4_humidity = condition['main']['humidity']
            self.p4_visibility = condition['main']['humidity']
            self.p4_wind_degree = condition['wind']['deg']
            self.p4_wind_speed = condition['wind']['speed']
        else:
            raise Exception('No city left to add weather condition')
    
    def __repr__(self):
        return "Route->Attributes: " + str(vars(self))
