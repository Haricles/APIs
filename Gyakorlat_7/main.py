import requests

URL="https://api.genderize.io"
payload={"name": input("Kerem a nevet: ")}
resp=requests.get(URL,params=payload)
resp=resp.json()

print ("Te a",payload["name"],"nevet választottad!")
print ("A választott neved neme:",resp["gender"],"\nErre az esélye:",(resp["probability"]*100),"%")

URL_2="https://api.nationalize.io/"
payload_2={"name":payload}
resp_2=requests.get(URL_2,params=payload)
resp_2=resp_2.json()

lista=[]
for elem in resp_2["country"]:
    lista.append(elem["probability"])

def maximum(lista):
    legnagyobb=lista[0]
    for elem in lista:
        if legnagyobb < elem:
            temp=legnagyobb
            legnagyobb=elem
            elem=temp
    return legnagyobb

for elem in resp_2["country"]:
    if elem["probability"]== maximum(lista):
        print ("A választott neved nemzetisége:",elem["country_id"],"\nErre az esélye:",(maximum(lista)*100),"%")
