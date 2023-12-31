import random
import os
import math

print(" ")
print("Gyakorlás")
print(" ")

szam1 = random.randint (1,100)
szam2 = random.randint (1,100)
szam3 = random.randint (1,100)
print(szam1, szam2, szam3)
print(f"A három szám összege: ", szam1+szam2+szam3)
print(" ")
szam4 = random.randint (-100,0)
print(szam4)
print(" ")
print(" ")
ora1 = random.randint (0,24)
perc1 = random.randint (0,60)
mp1 = random.randint (0,60)
ora2 = random.randint (0,24)
perc2 = random.randint (0,60)
mp2 = random.randint (0,60)
elso = ora1*60*60+perc1*61+mp1
masodik = ora2*60*60+perc2*60+mp2
print(f" {ora1}:{perc1}:{mp1}; {ora2}:{perc2}:{mp2}")
print(f"A két időpont közti különbség {abs(elso-masodik)} mp.")
print(" ")
print(" ")
atmero = random.randint (10, 35)
print(f"A dinnye átmérője {atmero} cm.")
dinnye_k = atmero*math.pi
dinny_hossz = 2*dinnye_k + 60
mennyiseg = random.randint(2,100)
szalag = mennyiseg*dinny_hossz
print(f"{mennyiseg} dinnyéhez {round(szalag)} cm szallagra lesz szükség")
print(" ")
print(" ")
#valos = float(input("Adjon meg egy valós számot: "))
#print(f"A megadott szám a {math.floor(valos)} és a {math.ceil(valos)} számok között van, de a {round(valos)} számhoz van közelebb.")
#print(f"A szám egész része: {int(valos)}")
#print(f"A szám tört része: {valos - math.floor(valos)}")

print(" ")
print("21. feladat")
print(" ")

#osszegFt = float(input("Adjon meg egy Forint összeget: "))
#print(f"{osszegFt} Ft {osszegFt/384} Eurót, és {osszegFt/360} Dollárt ér.")

print(" ")
print("22. feladat")
print(" ")

#x1 = float(input("Adja meg az első pont x koordinátáját: "))
#y1 = float(input("Adja meg az első pont y koordinátáját: "))
#x2 = float(input("Adja meg a második pont x koordinátáját: "))
#y2 = float(input("Adja meg a második pont y koordinátáját: "))
#print(f"A két pont közti távolság", ((x2-x1)**2+(y2-y1)**2)**0.5)

print(" ")
print("23. feladat")
print(" ")

#nev1 = (input("Adja meg az első személy nevét!"))
#tomeg1 = float(input(f"Adja meg {nev1} testtömegét: "))
#magassag1 = float(input(f"Adja meg {nev1} magasságát: "))/100
#nev2 = (input("Adja meg a második személy nevét!"))
#tomeg2 = float(input(f"Adja meg {nev2} testtömegét: "))
#magassag2 = float(input(f"Adja meg {nev2} magasságát: "))/100
#nev3 = (input("Adja meg a harmadik személy nevét!"))
#tomeg3 = float(input(f"Adja meg {nev3} testtömegét: "))
#magassag3 = float(input(f"Adja meg {nev3} magasságát: "))/100
#print(f"Az átlagmagasság {round((magassag1+magassag2+magassag3)/3,2)} cm.")
#print(f"A testössztömeg {tomeg1+tomeg2+tomeg3} kg.")
#tti1 = tomeg1/magassag1**2
#tti2 = tomeg2/magassag2**2
#tti3 = tomeg3/magassag3**2
#print(f"{nev1} testtömeg indexe: {tti1}")
#print(f"{nev2} testtömeg indexe: {tti2}")
#print(f"{nev3} testtömeg indexe: {tti3}")
#tti_k = (tti1, tti2, tti3)
#print(f"A legelhízottabb személy tti mértéke {max(tti_k)}")

print(" ")
print("24. feladat")
print(" ")

havi_fogy = float(input("Ajda meg a havi átlagos villanyszámlájának összegét: "))
eves_fogy = havi_fogy*12
print(f"Az éves energiaköltsége ezek alapján kb. {eves_fogy} Ft.")
eves_villany = eves_fogy/39
print(f"Az éves energiafelhasználása pedig kb. {eves_villany} kWh.")
napelem_naponta = 310*24/1000
napelem_eves = napelem_naponta*360
szukseges_napelem = math.floor(eves_villany/napelem_eves)
print(f"Ha az éves fogyasztásának kb. 85%-át szeretné kitermelni napelemekkel, {szukseges_napelem} napelemre van szükség.")
teto = szukseges_napelem*1.7
print(f"Ennyi napelemhez minimum {teto} nm2 tetőfelületre van szükség.")

print(" ")
print("25. feladat")
print(" ")

ingatlan_ertek = float(input("Adja meg a vásárolni kívánt ingatlan értékét: "))
ügynök = ingatlan_ertek*0.0275
ügyvéd = ingatlan_ertek*0.015
illetek = ingatlan_ertek*0.04
energetikai = 40000
földhivatal = 6600
print(f"Ha az ingatlan értéke {ingatlan_ertek} Ft, akkor")
print(f"- {ügynök} Ft az ingatlan ügynök,")
print(f"- {ügyvéd} Ft az ügyvéd,")
print(f"- {illetek} Ft az ingatlan illeték,")
print(f"- {energetikai} Ft az energetikai tanusítvány,")
print(f"- {földhivatal} Ft a tulajdoni lap,")
print(f"És így az ingatlan teljes összege a felmerülő díajakkal együtt {ingatlan_ertek+ügynök+ügyvéd+illetek+energetikai+földhivatal} Ft.")