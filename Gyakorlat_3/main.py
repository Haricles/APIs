'''
Készíts egy programot, amely a RandomUser API felhasználásával véletlenszerűen megjelenít egy nevet,
és a felhasználónak ki kell találnia, hogy féréfiről vagy nőröl van-e szó. A program természetesen értékelje a választ!
'''
import requests

def get_gender(name):
    gen_url = 'https://api.genderize.io/'
    payload = {'name': name}
    gen_resp = requests.get(gen_url, params=payload)
    gender = gen_resp.json()['gender']
    gen_prob = gen_resp.json()['probability']
    return gender, gen_prob

def get_age(name):
    age_url = 'https://api.agify.io/'
    payload = {'name': name}
    age_resp = requests.get(age_url, params=payload)
    age = age_resp.json()['age']
    return age

def get_nat(name):
    nat_url = 'https://api.nationalize.io/'
    payload = {'name': name}
    nat_resp = requests.get(nat_url, params=payload)
    nat = nat_resp.json()['country'][0]['country_id']
    nat_prob = nat_resp.json()['country'][0]['probability']
    return nat, nat_prob

def random_nev():
    URL="https://randomuser.me/api/"
    resp=requests.get(URL)
    resp=resp.json()["results"][0]["name"]["first"]
    return resp

print('A keresztnév alapján kitalálom a személy nemét, korát és országát.')
first_name = random_nev()
print(f"A választott keresztnév: {first_name}")

print(f'A neme: {"férfi" if get_gender(first_name)[0] == "male" else "nő"}, '
      f'ennek valószínűsége: {get_gender(first_name)[1] * 100:.0f}%.')
print(f'A kor valószínűleg {get_age(first_name)} év.')
print(f'Az ország kódja: {get_nat(first_name)[0]}, '
      f'ennek valószínűsége: {get_nat(first_name)[1] * 100:.0f}%.')

