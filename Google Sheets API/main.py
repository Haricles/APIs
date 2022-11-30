'''
A mellékelt táblázat tartalmát először másold át egy Google-táblázatba! Készíts egy programot,
amely ezt a Google-táblázatot kiegészíti a felhasználók automatikusan generált e-mail címével,
melyben az ékezetes betűk ékezet nélkülivé vannak alakítva.
Az e-mail cím felépítése: vezeteknev.keresztnev@x_mail.com
Az adatbeolvasás dinamikusan történjen, tehát a program maga határozza meg az adatsorok számát!
Ügyelj arra is, hogy optimalizáld az API-hívások számát!
'''
import gspread
from pprint import pprint

def ekezet_mentesit(cim):
    mit= "áéíóöőúüű"
    mire="aeiooouuu"
    for index,betu in  enumerate(mit):
        cim=cim.replace(betu,mire[index])
    return cim

gc = gspread.service_account(filename="creds.json")
sh = gc.open("diakok").sheet1

diak_adatok=sh.get_all_records()

e_mail_cimek=[]
for diak in diak_adatok:
    e_mail_cim= diak["vezetéknév"]+"."+diak["keresztnév"]+"@x_mail.com"
    e_mail_cim=e_mail_cim.lower()
    e_mail_cim=ekezet_mentesit(e_mail_cim)
    e_mail_cimek.append([e_mail_cim])

sh.update_acell("C1","e-mail")
sh.update("C2:C"+str(len(e_mail_cimek)+1),e_mail_cimek)