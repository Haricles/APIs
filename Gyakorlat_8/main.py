import requests

class get_Name():
    def __init__(self, url, name):
        self.url = url
        self.name = name

    def get_requests_and_json(self):
        resp = requests.get(self.url, params={"name": self.name})
        resp = resp.json()
        return resp

    def printer(self):
        print("Te a", self.name, "nevet választottad!")
        print("A választott neved neme:", self.get_requests_and_json()["gender"])
        print("Erre az esély:", (self.get_requests_and_json()["probability"] * 100), "%")

class Nationalize():
    def __init__(self, url, name):
        self.url = url
        self.name = name

    def get_requests_and_json(self):
        resp = requests.get(self.url, params={"name": self.name})
        resp = resp.json()
        return resp

    def creat_list(self):
        lista = []
        for elem in self.get_requests_and_json()["country"]:
            lista.append(elem["probability"])
            return lista

    def maximum(self, lista):
        legnagyobb = lista[0]
        for elem in lista:
            if legnagyobb < elem:
                temp = legnagyobb
                legnagyobb = elem
                elem = temp
        return legnagyobb

    def printer(self):
        for elem in self.get_requests_and_json()["country"]:
            if elem["probability"] == self.maximum(self.creat_list()):
                print("A választott neved nemzetisége:", elem["country_id"], )
                print("Erre az esély:", self.maximum(self.creat_list()) * 100)

nev = get_Name("https://api.genderize.io", "Akos")
nev.printer()

nation = Nationalize("https://api.nationalize.io/", "Akos")
nation.printer()