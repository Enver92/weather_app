from django.shortcuts import render

import requests


def index(request):
    # key = 'c4e326863862fb255de9d3a95d485d53'
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Kiev&units=metric&appid=c4e326863862fb255de9d3a95d485d53'
    city = 'Kiev'
    raw_weather = requests.get(url.format(city)).json()
    city_weather = {
        'city': city,
        'temperature': raw_weather['main']['temp'],
        'description': raw_weather['weather'][0]['description'],
        'icon': raw_weather['weather'][0]['icon'],
    }
    context = {'city_weather': city_weather}
    return render(request, 'weather/weather.html', context)
