'''
Készíts egy programot, amely az Universities API felhasználásával megjeleníti a felhasználó által
megadott országbn található egyetemek nevét és honalapcímét!
'''
import requests
from pprint import pprint

URL="http://universities.hipolabs.com/search"
payload={"country":"hungary"}

resp=requests.get(URL,params=payload)
resp=resp.json()

for elem in resp:
    print(elem["web_pages"],elem["name"])