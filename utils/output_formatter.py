from datetime import datetime

def format_weather_data(data):
    try:
        return f"""
{data['name']} Hava Durumu ({datetime.utcfromtimestamp(data['dt']).strftime('%H:%M UTC')}):
- Sıcaklık: {data['main']['temp']}°C (Hissedilen: {data['main']['feels_like']}°C)
- Nem: {data['main']['humidity']}%
- Rüzgar: {data['wind']['speed']} m/s
- Gökyüzü: {data['weather'][0]['description'].capitalize()}
"""
    except KeyError as e:
        return f"Eksik veri: {str(e)}"