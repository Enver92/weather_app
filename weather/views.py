from django.shortcuts import render

from .models import City
import requests


def index(request):
    # key = 'c4e326863862fb255de9d3a95d485d53'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c4e326863862fb255de9d3a95d485d53'

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        raw_weather = requests.get(url.format(city)).json()
        city_weather = {
            'city': city.name,
            'temperature': raw_weather['main']['temp'],
            'description': raw_weather['weather'][0]['description'],
            'icon': raw_weather['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    context = {'weather_data': weather_data}
    return render(request, 'weather/weather.html', context)
