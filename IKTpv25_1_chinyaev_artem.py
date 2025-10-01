#1.
#Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
#Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
#Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
#“Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”

# print ("tere maailm!")
# nimi=input("Sisseta oma nimi: ").capitalize()#sisend ja ootab enterit
# print(f"Tere maailm! tervitan sind {nimi}")
# vanus=int(input("siseta oma vanus: "))#int teisendab stringi täis arvuks
# print(f"tere maailm! tervistan sind {nimi.upper()}. sa oled {vanus} aastat vana") #upper teeb suurtähted
# print(f"tere mailm! tervistan sind {nimi.lower()}. sa oled {vanus} aastat vana") #lower

#2
#Mis tüüpi on järgnevad muutujad:
#a) vanus = 18
#b) eesnimi = "Jaak"
#c) pikkus = 16.5
#d) kas_käib_koolis = True
#Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
#Kirjuta kood tüüpide kontrollimiseks.
# vanus = 18           #int
# eesnimi = "jaak"     #str
# pikkus = 1.65        #float
# kas_käib_koolis = True #bool
# print(f"vanus {vanus} on:{type(vanus)}")
# print(f"eesnimi {eesnimi} on: {type(eesnimi)}")
# print(f"pikkus {pikkus} on: {type(pikkus)}")
# print(f"kas_käib_koolis {kas_käib_koolis} on: {type(kas_käib_koolis)}")

#3

#Kirjuta enda koodis laual olevate kommide arv muutujasse(kommide arv on juhuslik). Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
#Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, kui palju komme laual nüüd on. 
from enum import member
from random import *
from types import MemberDescriptorType
laua_peal=randint(10,50)#juhuslik arv 10-50
print(f"laual on {laua_peal} kommi")
võtab=int(input("mitu kommi soovid võtta? "))#sisend võtab teisendab stringi täisarvuks
laua_peal-=võtab #laua_peal=laua_peal-võtab, võtab kommid maha
print(f"laual on nüüd {laua_peal} kommi")

# 4
# Puu läbimõõdu arvutamine
# Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.
from math import*
ümbermõõt=int(input("sisesta puu ümbermõõt meetrites: ")) #int teisendab stringi täisarvuks

läbimõõt=ümbermõõt/3.14 #läbimõõt=ümbermõõt/π
print(f"puu läbimõõt on {läbimõõt:.2f} meetrit") #:.2f tähendab 2 kohta pärast koma

läbimõõt=ümbermõõt/pi #voib kasutada ka math raamatukogu
print(f"puu läbimõõt on {läbimõõt:.2f} meetrit") #.2f tähendab 2 kohta pärast koma

# 5.
# Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
# from math import*
# N=int(input("sisesta maatüki N külje pikkus meetrites: "))
# M=int(input("sisesta maatüki M külje pikkus meetrites: "))
# diagonaal=sqrt(N**2+M**2) #Pythagorase teoreem
#     t(f"maatüki diagonaal on {diagonaal:.2f} meetrit")


