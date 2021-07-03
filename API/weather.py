from Keys import api_keys
import geocoder
from meteostat import Point, Daily, Monthly, Normals
from meteostat import Hourly
from static import LejziTime as lTime

ApiKeys = api_keys.ApiKeys
lt = lTime()
last_week = lt.week_back(lt.today)


class Weather:

    def __init__(self, start_end, cities_ll):
        if len(cities_ll) > 1:
            self.cities = [Point(cor[0], cor[1]) for cor in cities_ll]
        else:
            self.cities = [Point(cities_ll[0], cities_ll[1])]
        self.start = start_end[0]
        self.end = start_end[1]
        self.hourly_keys = ['station', 'time', 'temp', 'rhum', 'prcp', 'wdir',
                            'wspd', 'pres', 'coco', 'dwpt', 'snow', 'wpgt', 'tsun']
        self.daily_keys = [['tavg', 'tmin', 'tmax', 'prcp', 'snow', 'wdir', 'wspd', 'pres', 'wpgt', 'tsun']]
        self.drop_keys = []

    def daily(self):
        f = 'daily'
        data = [Daily(city, self.start, self.end).fetch() for city in self.cities]
        return f, data

    def monthly(self):
        f = 'daily'
        data = [Monthly(city, self.start, self.end).fetch() for city in self.cities]
        return f, data

    def hourly(self):
        f = 'hourly'
        data = [Hourly(city, self.start, self.end).fetch() for city in self.cities]
        return f, data


def city_ll(city_name):
    # <3 href='https://locationiq.com'>Search by LocationIQ.com <3 much love #
    g = geocoder.locationiq(city_name, key=ApiKeys.weather).latlng
    return g


def wh_data(time_spectrum=last_week, cities=None, period='Daily'):
    if cities:
        cities_lngltd = []

        if type(cities) == str:
            cities = [cities]
        for i, city in enumerate(cities):
            city = cities[i]
            city = city_ll(city)
            cities_lngltd.append(city)

        cities_weather = Weather(time_spectrum, cities_lngltd)
        if period == 'Daily':
            cities_weather = cities_weather.daily()[1]
        if period == 'Hourly':
            cities_weather = cities_weather.hourly()[1]
        weather_data = {}
        for i, city in enumerate(cities):
            city = city + 'W'
            weather_data[city] = cities_weather[i]
        return weather_data

    else:
        cities = ['Warszawa', 'Wrocław']
        cities = [city_ll(city) for city in cities]
        cities_weather = [Weather(time_spectrum, city) for city in cities]
        return cities_weather


def get_weather_data(**kwargs):
    list_of_weathers = wh_data(**kwargs)
    return list_of_weathers


if __name__ == '__main__':
    # returns dict :: {'City Name' : pandas.core.frame.DataFrame}
    x = get_weather_data(cities=['London', 'New York'])
