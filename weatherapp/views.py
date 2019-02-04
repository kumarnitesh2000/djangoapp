import requests
from django.shortcuts import render

def index1(request):
 url= 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=f26e3ccb35773694fcb91030421610b0'
 city = 'delhi'
 r = requests.get(url.format(city)).json()

 city_weather = {
  'city' : city ,
  'temperature' : r['main']['temp'],
  'description': r['weather'][0]['description'],
  'icon' : r['weather'][0]['icon'],
 }
 context =  {'city_weather':city_weather}
 print(city_weather)
 return render(request,'weatherapp/index1.html',context)
