'''

'''
import requests
from pprint import pprint

def get_weather(varos):
    API_KEY=input("Kerem az API kulcsot: ")
    URL="https://api.openweathermap.org/data/2.5/weather"
    payload={"q":varos,"appid":API_KEY,"lang":"HU","units":"metric"}
    resp=requests.get(URL,params=payload)
    resp=resp.json()
    homerseklet=resp["main"]["temp"]
    leiras=resp["weather"][0]["description"]
    return f"{varos}: jelenleg {homerseklet} C° van és {leiras}."

def get_air(x,y):
    API_KEY = input("Kerem az API kulcsot: ")
    URL="https://api.openweathermap.org/data/2.5/air_pollution"
    payload = {"lat":x,"lon":y, "lang": "HU", "units": "metric","appid": API_KEY}
    resp=requests.get(URL,params=payload)
    resp=resp.json()
    for elem in resp["list"]:
        if elem["components"]["pm10"] < 25:
            return "Jó minőségű a levegő!"
        if (elem["components"]["pm10"] >= 25) and elem["components"]["pm10"] < 50:
            return "Nem rossz a levegő!"
        if (elem["components"]["pm10"] >= 50) and elem["components"]["pm10"] < 90:
            return "Még elfogadható!"
        if (elem["components"]["pm10"] >= 90) and elem["components"]["pm10"] < 180:
            return "Rossz a levegő minősége!"
        if elem["components"]["pm10"] > 180:
            return "Nagyon rossz a levegő minősége!"

pprint(get_air(28.644800,77.216721))
pprint(get_weather("Budapest"))
