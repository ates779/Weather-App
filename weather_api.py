import requests
from utils.config_handler import get_api_key

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city_name):
    api_key = get_api_key()
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',
        'lang': 'tr'
    }
    
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()  # HTTP hatalarını main'e aktar
    return response.json()