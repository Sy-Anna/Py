import random

"""
szam = int(input("szam= "))
osszeg = 0
while szam!=0:
    osszeg += szam
    szam = int(input("szám= "))
print(osszeg)
"""

"""
osszeg=0
while True:
    szam = int(input("szam= "))
    osszeg += szam
    if szam==0:
        break
print(osszeg)
"""

"""
i = 1
while i <= 10:
    print(i, end=" ")
    i+=1
"""
"""
print("Fej vagy írás játék")
while True:
    veletlen = random.randint(0,1)
    tipp = int(input("tipp: "))
    if veletlen == tipp:
        print("Gratulálok!")
        break
    else:
        print("Nem talált!\n\n Próbálja újra!")
"""

"""
szoveg = "alma"
while True:
    szo=input("Szó: ")
    szoveg+=" "+szo
    if szo==" ":
        break
print(szoveg)
"""

"""
print("Szám kitalálós játék")
print("Nehézségi szint: könnyű, nehéz, vagy hardcore?")
valasz = input("A válaszom: ")
if valasz == "könnyű":
    szam = random.randint(1, 10)    
if valasz == "nehéz":
    szam = random.randint(1, 100)
if valasz == "hardcore":
    szam = random.randint(1, 1000)
elet = 7
while True:
    print(f"Életek száma: {elet}")
    tipp = int(input("tipp= "))
    if tipp == szam:
        print("Gratulálok!")
        break
    else:
        elet-=1
        print("Nem jó!")
    if elet == 0:
        print("Elfogytak az életeid!")
        break
"""
              

