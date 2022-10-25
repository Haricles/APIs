'''
Írj egy programot, amely az IPinfo nevű API segítségével adatokat ír ki a felhasználó által megadott IP címről.
'''
import requests
from pprint import pprint

URL="https://ipinfo.io/"
ip=input("Kerem az ip címet: ")
new_url=URL+ip
resp=requests.get(new_url)
resp=resp.json()
pprint(resp)


