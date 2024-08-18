from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.views.decorators.cache import never_cache
from datetime import date
# Create your views here.
@never_cache
def weather(request):
    if request.method=='POST':
        city=request.POST['city']
        api_key='xxx'
        url = f"xxxxxx"
        response = requests.get(url)
        data = response.json()
        tdate=date.today().isoformat
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description'].capitalize()
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        return render(request,'main.html',{'date':tdate,
                                           'city':city,
                                           'temperature':temperature,
                                           'weatherdesc':weather_description,
                                           'humidity':humidity,
                                           'wind_speed':wind_speed})
    tdate=date.today().isoformat
    return render(request,'main.html',{'date':tdate})