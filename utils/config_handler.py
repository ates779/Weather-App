import configparser
import os

def get_api_key():
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.ini')
    
    if not os.path.exists(config_path):
        raise FileNotFoundError("config.ini dosyası bulunamadı!")
    
    config.read(config_path)
    return config['API']['api_key']