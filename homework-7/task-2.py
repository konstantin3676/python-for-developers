import requests

OPENWEATHER_API_KEY = ""

def get_coordinates(city_name, api_key):
    geocode_url = "https://api.openweathermap.org/geo/1.0/direct"
    params = {
        'q': city_name,
        'limit': 1,
        'appid': api_key
    }
    response = requests.get(geocode_url, params=params)
    if response.status_code != 200:
        return None
    data = response.json()
    if not data:
        return None
    return data[0]['lat'], data[0]['lon']

def get_weather_by_coords(lat, lon, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru'
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None
    return response.json()

def main():
    api_key = OPENWEATHER_API_KEY

    city = input("Введите название города: ").strip()
    if not city:
        print("Название города не может быть пустым.")
        return

    coords = get_coordinates(city, api_key)
    if not coords:
        print("Город не найден. Проверьте правильность написания.")
        return

    lat, lon = coords
    print(f"Найдены координаты: {lat}, {lon}")

    weather_data = get_weather_by_coords(lat, lon, api_key)
    if not weather_data:
        print("Не удалось получить данные о погоде.")
        return

    temp = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']

    print(f"Погода в городе {city}:")
    print(f"Температура: {temp}°C")
    print(f"Описание: {description.capitalize()}")

if __name__ == "__main__":
    main()