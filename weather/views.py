from django.shortcuts import render

from .models import City
from .forms import CityForm
from .key import key
import requests


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + key

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    print(cities)
    weather_data = []

    for city in cities:
        raw_weather = requests.get(url.format(city.name)).json()
        print(raw_weather)
        city_weather = {
            'city': city.name,
            'temperature': raw_weather['main']['temp'],
            'description': raw_weather['weather'][0]['description'],
            'icon': raw_weather['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)
