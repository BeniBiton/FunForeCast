from backend.adapters.gpt_adapter import get_recommended_temperature
from backend.adapters.weather_adapter import get_weather_by_date
from backend.api.models import DateModel


def calculate_best_date(attraction: str, dates: DateModel, city):
    preferred_temperature = get_recommended_temperature(attraction)
    dates_temperature = get_weather_by_date(dates.start_date, dates.end_date, city)
    temp_diff = [(date ,abs(float(temperature.replace("°C",""))-preferred_temperature)) for date, temperature in dates_temperature.items()]
    if min(temp_diff, key=lambda tup: tup[1]) < 10:
            date_index = temp_diff.index(min(temp_diff, key=lambda tup: tup[1]))
            return temp_diff[date_index][0]
