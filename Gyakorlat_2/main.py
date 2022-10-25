'''
A program írja ki képernyőre, hogy a SuliPY oldal mikor frissült utoljára!
Tipp: Ez az információ is a response header részében található.
'''
import requests

resp=requests.get("https://sulipy.hu/")
resp=resp.headers
for key,value in resp.items():
    if key=="Date":
        print(f"Az oldal ekkor frissült utoljára: {value}")

