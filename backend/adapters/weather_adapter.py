import requests
from backend.consts import *


def get_weather_by_date(start, end,city):
    for station in get_stations_by_longlat(city):
        querystring = {
            "station": station,
            "start": start,
            "end": end
        }

        response = requests.get(WEATHER_ENDPOINT, headers=WEATHER_API_HEADERS, params=querystring)

        weather_data = response.json()
        temperature_results = {}
        try:
            for key in range(0, 6):

                date = weather_data["data"][key]["date"]
                temperature = weather_data["data"][key]["tavg"]
                temperature_results[date] = float(temperature)
        except Exception:
            pass
        return temperature_results


def get_longlat(city):
    convert_params = {
        "q": city,
        "key": CONVERT_API_KEY
    }

    response = requests.get(url=CONVERT_ENDPOINT, params=convert_params)
    convert_data = response.json()
    _,lat,lng = convert_data["results"][0]["annotations"]["OSM"]["edit_url"].rsplit("/", 2)
    longlat = (lat,lng)
    return longlat


def get_stations_by_longlat(city):
    station_params = {
        "lat": get_longlat(city)[0],
        "lon": get_longlat(city)[1],
        "limit": 1
    }

    response = requests.get(url=STATION_ENDPOINT, headers=WEATHER_API_HEADERS, params=station_params)
    station_data = response.json()
    station_ids = list()
    for station in station_data["data"]:
        station_ids.append(station["id"])
    return station_ids
