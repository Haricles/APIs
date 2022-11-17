import deepl
import requests

#Translator API
auth_key = "e30aafc4-e428-53d5-a7a8-14bd75d68dc7:fx"
translator = deepl.Translator(auth_key)

#Random World API
url="https://random-word-api.herokuapp.com/word"
english_word=requests.get(url).text

life_number=3
pontszam=0

while life_number > 0:
    english_word = str(english_word)
    print (f"A kitalálandó szó: {english_word}")
    hungary_word = str(input("Kerem a fordítását:"))
    hu_en = translator.translate_text(hungary_word, source_lang="HU", target_lang="EN-US")
    en_hu = translator.translate_text(english_word, source_lang="EN", target_lang="HU")
    if english_word == hu_en:
        pontszam+=1
    else:
        english_word=requests.get(url).text
        life_number-=1

print ("A játék vége.")
print (f"Pontszám: {pontszam}")
print (f"Életek száma:{life_number}")


