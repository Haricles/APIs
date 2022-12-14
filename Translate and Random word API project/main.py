import deepl
import requests

#Translator API
auth_key = "e30aafc4-e428-53d5-a7a8-14bd75d68dc7:fx"
translator = deepl.Translator(auth_key)

#Random World API
url="https://random-word-api.herokuapp.com/word"
english_word=requests.get(url).text

life_number=3
score=0

while life_number > 0:
    english_word = str(english_word)
    print (f"A kitalálandó szó: {english_word}")
    hungary_word = str(input("Kerem a fordítását:"))
    en_hu = str(translator.translate_text(english_word, source_lang="EN", target_lang="HU"))
    if hungary_word == en_hu:
        score+=1
    else:
        english_word=requests.get(url).text
        life_number-=1

print ("A játék vége.")
print (f"Pontszám: {score}")
print (f"Életek száma:{life_number}")