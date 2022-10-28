import requests
from pprint import pprint
from datetime import datetime

API_KEY = input("Kerem az API kulcsot: ")

def get_weather(city):
    try:
        URL = "https://api.openweathermap.org/data/2.5/weather"
        payload = {"q": city, "appid": API_KEY, "lang": "HU", "units": "metric"}
        resp = requests.get(URL, params=payload)
        resp = resp.json()
        homerseklet = resp["main"]["temp"]
        leiras = resp["weather"][0]["description"]
        return f"{city}: jelenleg {homerseklet} C° van és {leiras}."
    except KeyError:
        return "Nem létező hely vagy számot adtál meg!"

def geo_cord(city):
    URL = "http://api.openweathermap.org/geo/1.0/direct"
    payload = {"q": city, "limit": 20, "appid": API_KEY}
    resp = requests.get(URL, params=payload)
    resp = resp.json()
    for adat in resp:
        lat = adat["lat"]
        lon = adat["lon"]
    return lat, lon

def get_air(city):
    try:
        URL = "https://api.openweathermap.org/data/2.5/air_pollution"
        payload = {"lat": geo_cord(city)[0], "lon": geo_cord(city)[1], "lang": "HU", "units": "metric",
                   "appid": API_KEY}
        resp = requests.get(URL, params=payload)
        resp = resp.json()
        for elem in resp["list"]:
            if elem["components"]["pm10"] < 25:
                return "Nagyon jó a levegő minősége!"
            if (elem["components"]["pm10"] >= 25) and elem["components"]["pm10"] < 50:
                return "Nem rossz a levegő minősége!"
            if (elem["components"]["pm10"] >= 50) and elem["components"]["pm10"] < 90:
                return "Még elfogadható a levegő minősége!"
            if (elem["components"]["pm10"] >= 90) and elem["components"]["pm10"] < 180:
                return "Rossz a levegő minősége!"
            if elem["components"]["pm10"] > 180:
                return "Nagyon rossz a levegő minősége!"
    except UnboundLocalError:
        return "Nem létező hely vagy számot adtál meg!"
    except TypeError:
        return "Nem adtál meg települést!"

def sunrise_sunset(city):
    try:
        URL = "https://api.openweathermap.org/data/2.5/weather"
        payload = {"q": city, "appid": API_KEY, "lang": "HU", "units": "metric"}
        resp = requests.get(URL, params=payload)
        resp = resp.json()
        for elem in resp:
            sunrise = resp["sys"]["sunrise"]
            sunset = resp["sys"]["sunset"]
        return f"A napfelkelte:{datetime.fromtimestamp(sunrise)} Napnyugta:{datetime.fromtimestamp(sunset)}"
    except:
        return "Nem létező hely vagy számot adtál meg"

def change_list(city):
    URL = "http://api.openweathermap.org/data/2.5/forecast/"
    payload = {"lat": geo_cord(city)[0], "lon": geo_cord(city)[1], "appid": API_KEY, "units": "metric", }
    resp = requests.get(URL, params=payload)
    resp = resp.json()
    temp_list = []
    i = 0
    for elem in range(len(resp["list"])):
        temp = resp["list"][i]["main"]["temp"]
        temp_list.append(temp)
        i += 1
    return temp_list

def minimum(temp_list):
    legkisebb = temp_list[0]
    for elem in temp_list:
        if legkisebb > elem:
            legkisebb = elem
    return f"Az 5 nap legkisebb mért hőmérséklete:{legkisebb}C°"

def arrangement(temp_list):
    for elotte in range(len(temp_list) - 1):
        for mogotte in range(elotte + 1, len(temp_list)):
            if temp_list[elotte] > temp_list[mogotte]:
                temp = temp_list[elotte]
                temp_list[elotte] = temp_list[mogotte]
                temp_list[mogotte] = temp
    return f"Az 5 nap alatt mért hőmérsékletek növekvő sorrendben: {temp_list}"

def average(temp_list):
    osszeg = 0
    for elem in temp_list:
        osszeg += elem
    return f"A mért adatok alapján az átlag hőmérséklet az elmúlt 5 napban:{osszeg / len(temp_list)}C°"

def get_print(city):
    pprint(get_weather(city))
    pprint(sunrise_sunset(city))
    pprint(get_air(city))
    pprint(minimum(change_list(city)))
    pprint(arrangement(change_list(city)))
    pprint(average(change_list(city)))

get_print("Buják")

