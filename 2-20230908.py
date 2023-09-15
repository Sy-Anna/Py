print("1. feladat")
print(" ")
print("""
         *
        ***
       *****
      *******
    """)
print(" ")
print("------------")
print(" ")
print("2. feladat")
# a változó mindig beüvel kezdődik, ékezet nélküli és kisbetűs, a neve utal a tartalomra (pl ha nevet akarok tárolni legyen a változó neve "nev")
# minden szöveges érték "..." között legyen!!
nev = "Anna"
magassag = 176
szuletesi_ev = 2004
szuletesiEv = 2004
SzuletesiEv = 2004
# mindhárom megoldás külön változó, azaz mindhárom érték elfoglal eg yhelyez a memóriában

print(type(nev))
print(type(magassag))
print(type(szuletesi_ev))
# kiiratásnál  type(változó)
# szöveges értéknél a type string, a 
# számos értéknél valós számok, alapértelmezett beállítás szerint ponttal elválasztva pl. 176.2 -> type float lesz
magassag2 = 163.5
print(type(magassag2))
print(" ")
# type-ot ne cseréljünk mert az nem jó, ha egyszer 

print("A neved:" +nev) #konkatenáció: összefűzés
print("A neved", nev)
print("A magasságod:", magassag)
print("A magasságod: "+str(magassag))
print(f"A neved: {nev}")
# f = format
# { valamire hivatkozik, itt a változóra
print(f"A neved: {nev}, magasságod: {magassag} cm, születési éved: {szuletesi_ev}")

eletkor = 2023 - szuletesi_ev
print(f"az életkorod: {eletkor}")
# matematikai műveleteket végezhetünk

print(" ")
print("-------------------")
print(" ")
print("3. feladat")
print(" ")
# deklarizáció  = változót hozok létre
# inicializáció = a változónak kezdeti értéket adok
a = 5
b = 10
print(f"a = {a}, b = {b}")
print(f"a = {a}, b = {b*2}")
print(b)
b = b*2
print(b)
a = a+1
a += 1
print(" ")
# műveleti jelek = operátorok
# = értékadó operátok
# += összevont értékadó operátor
# aritmetikai operátorok: + - > / // %
c = 10
print(f"{c/3}") # rendes osztás: valós számok: float
print(f"{c//3}") # egészrész osztás: levágja a maradékot
print(f"{c%3}") # csak a maradékot kapjuk meg eredményül