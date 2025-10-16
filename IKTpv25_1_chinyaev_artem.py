# #1.
# #Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
# #Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
# #Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
# #“Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”

# # print ("tere maailm!")
# # nimi=input("Sisseta oma nimi: ").capitalize()#sisend ja ootab enterit
# # print(f"Tere maailm! tervitan sind {nimi}")
# # vanus=int(input("siseta oma vanus: "))#int teisendab stringi täis arvuks
# # print(f"tere maailm! tervistan sind {nimi.upper()}. sa oled {vanus} aastat vana") #upper teeb suurtähted
# # print(f"tere mailm! tervistan sind {nimi.lower()}. sa oled {vanus} aastat vana") #lower

# #2
# #Mis tüüpi on järgnevad muutujad:
# #a) vanus = 18
# #b) eesnimi = "Jaak"
# #c) pikkus = 16.5
# #d) kas_käib_koolis = True
# #Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
# #Kirjuta kood tüüpide kontrollimiseks.
# # vanus = 18           #int
# # eesnimi = "jaak"     #str
# # pikkus = 1.65        #float
# # kas_käib_koolis = True #bool
# # print(f"vanus {vanus} on:{type(vanus)}")
# # print(f"eesnimi {eesnimi} on: {type(eesnimi)}")
# # print(f"pikkus {pikkus} on: {type(pikkus)}")
# # print(f"kas_käib_koolis {kas_käib_koolis} on: {type(kas_käib_koolis)}")

# #3

# #Kirjuta enda koodis laual olevate kommide arv muutujasse(kommide arv on juhuslik). Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
# #Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, kui palju komme laual nüüd on. 
# from enum import member
# from random import *
# from types import MemberDescriptorType
# laua_peal=randint(10,50)#juhuslik arv 10-50
# print(f"laual on {laua_peal} kommi")
# võtab=int(input("mitu kommi soovid võtta? "))#sisend võtab teisendab stringi täisarvuks
# laua_peal-=võtab #laua_peal=laua_peal-võtab, võtab kommid maha
# print(f"laual on nüüd {laua_peal} kommi")

# # 4
# # Puu läbimõõdu arvutamine
# # Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.
# from math import*
# ümbermõõt=int(input("sisesta puu ümbermõõt meetrites: ")) #int teisendab stringi täisarvuks

# läbimõõt=ümbermõõt/3.14 #läbimõõt=ümbermõõt/π
# print(f"puu läbimõõt on {läbimõõt:.2f} meetrit") #:.2f tähendab 2 kohta pärast koma

# läbimõõt=ümbermõõt/pi #voib kasutada ka math raamatukogu
# print(f"puu läbimõõt on {läbimõõt:.2f} meetrit") #.2f tähendab 2 kohta pärast koma

# # 5.
# # Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
# # from math import*
# # N=int(input("sisesta maatüki N külje pikkus meetrites: "))
# # M=int(input("sisesta maatüki M külje pikkus meetrites: "))
# # diagonaal=sqrt(N**2+M**2) #Pythagorase teoreem
# #     t(f"maatüki diagonaal on {diagonaal:.2f} meetrit")
# # diagonaal=sqrt(N**2+M**2) #Pythagorase teoreem
# #     t(f"maatüki diagonaal on {diagonaal:.2f} meetrit")
# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = teepikkus / aeg

# print("Sinu kiirus oli " + str(kiirus) + " km/h")
# # Kood vastavalt esitatud plokkidele (ilma puhtuse ja vigade kontrollita)
# print("Sisesta palun viis täisarvu:")
# a1 = int(input("Arv 1: "))
# a2 = int(input("Arv 2: "))
# a3 = int(input("Arv 3: "))
# a4 = int(input("Arv 4: "))
# a5 = int(input("Arv 5: "))

# s = a1 + a2 + a3 + a4 + a5
# avg = s / 5

# print(f"\nViie sisestatud arvu summa on: {s}")
# print(f"Viie sisestatud arvu aritmeetiline keskmine on: {avg}")

# # Võimalik viga: kui jagamisarv on 0, tekib ZeroDivisionError
# d = int(input("\nSisesta üks täisarv, millega soovid summat jagada: "))

# tosa = s // d
# jaak = s % d

# print(f"Summa ({s}) jagatuna arvuga ({d}):")
# print(f"  Täisarvuline osa (kvoot): {tosa}")
# print(f"  Jääk: {jaak}")

# print("  @..@")
# print("  (----)")
# print(" ( \__/ )")
# print("^^ \"\" ^^")

# # Kolmnurk, korduv plokk
# x = 5
# y = 7
# z = 9
# P = x + y + z
# print(f"Kolmnurga küljed on a={x}, b={y}, c={z}.")
# print(f"Kolmnurga ümbermõõt P = a + b + c on: {P}")

# # Pitsa
# h = 12.90
# jp = 0.10

# try:
#     p = int(input("Mitu inimest (P) pitsa eest maksab? "))
# except ValueError:
#     exit() # Jätab veateate väljastamata

# if p <= 0:
#     exit() # Jätab teate väljastamata

# j = h * jp
# k = h + j
# m = k / p

# print(f"\n--- Arvutuse tulemused ---")
# print(f"Pitsa hind: {h:.2f} €")
# print(f"Jootraha (10%): {j:.2f} €")
# print(f"Kogu maksumus (koos jootrahaga): {k:.2f} €")
# print(f"Inimesi (P): {p}")
# print(f"Igaüks peab maksma: {m:.2f} €")

#1-esmaspäev, 2-teisipäev, 3-kolmapäev, 4-neljapäev, 5-reede, 6-laupäev, 7-pühapäev
#paev_number=int(input("Sisesta paeva number (1-7): "))
#if paev_number==1:
    #print("Esmaspaev")
#elif paev_number==2:
    #print("Teisipaev")
#elif paev_number==3:
    #print("Kolmapaev")
#elif paev_number==4:
    #print("Neljapaev")
#elif paev_number==5:
    #print("Reede")
#elif paev_number==6:
    #print("Laupaev")
#elif paev_number==7:
   # print("Puhapaev")
#else:
   # print("Vale number! Palun sisesta number vahemikus 1-7.")






#1. Juku

#a Kui eesnimi on Juku siis lähme Jukuga kinno. Aga teeme seda nii, kui nimi oli kirjutatud suurtähtedega.

#b Lisa valiku, kus Juku vanuse alusel otsustate mis pilet talle vaja osta. (Tee kontroll, kas sisestatud arv on täisarv)

#<6 aastad  - tasuta
#6-14 - lastepilet
#15-65 - täispilet
#>65 - sooduspilet
#<0 ja >100 viga andmetega
#eesnimi=input("Sisesta eesnimi: ")
#if eesnimi=="JUKU":
    #print("Lahme Jukuga kinno!")
    #vanus=input("Sisesta Juku vanus: ")
    #if vanus.isdigit():
        #vanus=int(vanus)
        #if vanus<9 or vanus>100:
            #print("Viga andmetega!")
        #elif vanus<6:
            #print("Pilet on tasuta!")
        #elif vanus<=14:
            #print("Lastepilet")
        #elif vanus<=65:
            #print("Taispilet")
        #else:
            #print("Sooduspilet")
    #else:
        #print("Palun sisesta vanus taisarvuna!")

#2 Pinginaabrid

#Küsi kahe inimese nimed. Kui nimed koosnevad
#ainult tähedest siis  teavita kasutajat,
#kas nad on täna pinginaabrid või ei mitte.
#nimi1=input("Sisesta nimi => ").capitalize()
#nimi2=input("Sisesta nimi => ").capitalize()
#if nimi1.isalpha() and nimi2.isalpha():
    #if nimi1=="Polina" and nimi2=="Darja" or nimi1=="Darja" and nimi2=="Polina":
        #print(f"{nimi1} ja {nimi2} on tana pinginaabrid")
    #else:
        #print(f"{nimi1} ja {nimi2} ei ole pinginaabrid")
#else:
    #print("Palun sisesta ainult tahed")

#3 Remont

#Küsi ristkülikukujulise toa seinte pikkused ning arvuta põranda pindala. Küsi kasutajalt remondi tegemise soov, kui ta on positiivne, siis küsi kui palju maksab ruutmeeter ja leia põranda vahetamise hind
#Lisaküsimus: kas ta teeb remonti ise või teeb seda professionaali abiga? Kui tegemist on professionaaliga, siis palun arvutage välja, kui palju remont koos tööga maksab.

#pikkus = int(input("Sisestage pikkus: "))
#laius = int(input("Sisestage laius: "))
#if pikkus>0 and laius>0:

    #pindala = pikkus * laius
    #print(f"pindala suurus on {pindala}")
    #user = input("Kas soovite remondi teha? ").capitalize()
    #if user.isalpha() and user == "Jah":
        #hind = float(input("Ruutmeetri hind? "))
        #if hind>0:
            #remondi_hind = hind * pindala
            #print(f"remondi summa on {remondi_hind}€")
            #kes = input("Kes teeb remondi(ise/tootaja)? ").capitalize()
            #if kes.isalpha() and kes == "Ise":
                #print(f"Siis summa on {remondi_hind}€")
            #else:
                #print(f"Siis summa on {remondi_hind + 300}€")
        #else:
            #print("Hind ei saa olla negatiivne!")
    #else:
        #print("Head aega!")
#else:
    #print("Arvud peavad olema suurem kui 0")

#4 Allahindus

 #Leia 30% soodustusega hinna, kui alghind on suurem kui 700



# hind = input("Hind: ")

# if hind.isdigit():
#     Hind = float(hind)
#     if hind>700:
#         hind * = 0.7
#         print(f"Soodus hind võrdub {hind}€")
# else:
#     print("on vaja numbri sissetsda") 

#     5 Temperatuur

# Küsi temperatuur ning teata, kas see on üle 18 kraadi (soovitav toasoojus talvel)
# temperatuur=int(input("Sisesta temperatuur: "))
# if temperatuur>18:
#     print("Temperatuur on soojem kui 18 kraadi")
#     elif temperatuur==18:
#      print("võib olla jahe")
# except:
#     print("palun siseta temperatuur ujukomaarvuna")
pikkus = int(input("Palun sisesta oma pikkus sentimeetrites: "))

pikkus = int(input("Palun sisesta oma pikkus sentimeetrites: "))

if pikkus < 160:
    print("Sa oled lühike.")
elif pikkus <= 185:
    print("Sa oled keskmise pikkusega.")
else:
    print("Sa oled pikk.")
#7 Pikkus ja sugu
#Küsi inimeselt pikkus ja sugu ning teata, kas ta on lühike, keskmine või pikk (mitu tingimusplokki võib olla üksteise sees).
f
