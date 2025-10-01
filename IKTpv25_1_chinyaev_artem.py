#1.
#Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
#Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
#Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
#“Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”

print ("tere maailm!")
nimi=input("Sisseta oma nimi: ").capitalize()#sisend ja ootab enterit
print(f"Tere maailm! tervitan sind {nimi}")
vanus=int(input("siseta oma vanus: "))#int teisendab stringi täis arvuks
print(f"tere maailm! tervistan sind {nimi.upper()}. sa oled {vanus} aastat vana") #upper teeb suurtähted
print(f"tere mailm! tervistan sind {nimi.lower()}. sa oled {vanus} aastat vana") #lower

#2
#Mis tüüpi on järgnevad muutujad:
#a) vanus = 18
#b) eesnimi = "Jaak"
#c) pikkus = 16.5
#d) kas_käib_koolis = True
#Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
#Kirjuta kood tüüpide kontrollimiseks.
vanus = 18           #int
eesnimi = "jaak"     #str
pikkus = 1.65        #float
kas_käib_koolis = True #bool
print(f"vanus {vanus} on:{type(vanus)}")
print(f"eesnimi {eesnimi} on: {type(eesnimi)}")
print(f"pikkus {pikkus} on: {type(pikkus)}")
print(f"kas_käib_koolis {kas_käib_koolis} on: {type(kas_käib_koolis)}")
