import math
import random

print("\n10. feladat\n")
"""
elso = int(input("Első elem: "))
diff = int(input("Differencia: "))
n = int(input("Elemszám: "))
szam = elso
for i in range (n):
    print(szam, end=", ")
    szam+=diff
"""
print("\n11. feladat\n")
"""
n = int(input("n= "))
szam = 1
while szam<n or szam==n:
    print(szam, end=", ")
    szam+=2
"""
print("\n12. feladat\n")
"""
n = int(input("n= "))
szorzo = 1
eredmeny = 1
while szorzo<=n-1:
    eredmeny*=szorzo
    print(szorzo, end="*")
    szorzo+=1
print(szorzo, "=", eredmeny)
"""

print("\n13. feladat\n")
"""
a = int(input("a= "))
b = int(input("b= "))
eredmeny = 0
for i in range (b):
    eredmeny+=a
print(f"{a} és {b} szorzata {eredmeny}")
"""
print("\n14. feladat\n")
"""
alap = int(input("hatványalap: "))
kitevo = int(input("Hatványkitevő: "))
eredmeny = alap
menny = 1
szamolo = alap
while menny<kitevo:
    szamolo*=alap
    eredmeny=szamolo
    menny+=1
print(f"{alap} {kitevo}. hatványa {eredmeny}")
"""
print("\n15. feladat\n")
"""
a=int(input("első szám: "))
b=int(input("második szám: "))
x,y=a,b
while b>0:
 r=a%b
 a=b
 b=r
print(f"gcd({x},{y})={a}")
""" #lopott
print("\n16. feladat\n")
"""
a=int(input("a= "))
b=int(input("b= "))
def lnko(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
 
def lkkt(a, b):
    o = lnko(a, b)
    return a * b // o
print(f"{a} és {b} legkisebb közös többszöröse {lkkt(a, b)}")
""" #lopott
print("\n17. feladat\n")
"""
szamlalo=int(input("számláló: "))
nevezo=int(input("nevező: "))
print(f"{szamlalo}/{nevezo}={szamlalo/nevezo}")
"""
print("\n18. feladat\n")
"""
eredmeny=0
even=0
odd=0
while eredmeny<=100:
    szam=int(input("Adjon meg egy számot: "))
    eredmeny+=szam
    if szam%2==0:
        even+=1
    else:
        odd+=1
print(f"{even} páros és {odd} páratlan számot adott meg.")
"""
print("\n20. feladat\n")
"""
while True:
    szam=int(input("Adjon meg egy páros számot: "))
    if szam%2==0:
        print("A szám megfelelő!")
        break
    else:
        print("Ez nem páros!")
"""
print("\n21. feladat\n")
"""
while True:
    szam=int(input("Adjon meg egy pozitív számot: "))
    if szam>0:
        print("Megfelelő szám!")
        print(f"{szam}/5 maradéka {szam%5}")
        break
    else:
        print("Nem megfelelő szám!")
"""
print("\n22. feladat\n")
"""
while True:
    szam=int(input("Adja meg a hét napját: "))
    if szam<1 or szam>7:
        print("Nem megfelelő szám!")
    else:
        if szam==1:
            nap="Hétfő"
        elif szam==2:
            nap="Kedd"
        elif szam==3:
            nap="Szerda"
        elif szam==4:
            nap="Csütörtök"
        elif szam==5:
            nap="Péntek"
        elif szam==6:
            nap="Szombat"
        elif szam==7:
            nap="Vasárnap"
        print(nap)
        break
"""
print("\n23. feladat\n")
"""
while True:
    szam=int(input("Adjon meg egy páratlan negatív számot: "))
    if szam>0:
        print("Nem megfelelő szám!")
    elif szam%2==0:
        print("Nem megfelelő szám!")
    else:
        print("Megfelelő szám!")
        break
"""
print("\n24. feladat\n")
"""
while True:
    szam=int(input("Adjon meg egy 3-mal és 5-tel osztható számot: "))
    if szam%5==0 and szam%3==0:
        print(f"{szam}/3={szam//3} és {szam}/5={szam//5}")
        break
    else:
        print("Nem megfelelő szám!")
"""
print("\n25. feladat\n")
"""
while True:
    szam=int(input("Adjon meg egy számot: "))
    if szam%5>0:
        print(f"{szam}/5 maradéka {szam%5}")
    else:
        print(f"{szam}/5 maradéka 0")
        break
"""
print("\n26. feladat\n")
"""
while True:
    szam1=int(input("Szám1: "))
    szam2=int(input("Szám2: "))
    if szam1==szam2:
        print("A két szám egyenlő!")
        break
    else:
        print(f"A nagyobb szám {max(szam1, szam2)}")
"""
print("\n27. feladat\n")
"""
while True:
    szam = random.randint(1,12)
    print(f"A szám {szam}")
    print(f"{szam}/3 maradéka {szam%3}")
    valasz=input("Kér új számot? (i/n) ")
    if valasz=="n":
        break
"""
print("\n28. feladat\n")
"""
while True:
    szam=int(input("Szám: "))
    if szam==0:
        break
"""
print("\n29. feladat\n")
"""
szam=random.randint(1,50)
while True:
    valasz=int(input("Melyik számra gondoltam? "))
    print()
    if szam==valasz:
        print("Helyes!")
        break
    elif szam>valasz:
        print("Nagyobb számra gondoltam!")
        print()
    elif szam<valasz:
        print("Kisebb számra gondoltam!")
        print()
"""
print("\n30. feladat\n")
"""
szam=random.randint(1,50)
elet=7
while elet>0:
    valasz=int(input("Melyik számra gondoltam? "))
    print()
    if szam==valasz:
        print("Helyes!")
        break
    elif szam>valasz:
        print("Nagyobb számra gondoltam!")
        print()
        elet-=1
    elif szam<valasz:
        print("Kisebb számra gondoltam!")
        print()
        elet-=1
if elet==0:
    print(f"{szam} számra gondoltam")
"""
print("\n31. feladat\n")

#nemtudom

print("\n32. feladat\n")
"""
szorzo=1
while True:
    alap=int(input("Alapszám: "))
    n=int(input("Meddig? "))
    if alap>0 and n>0:
        for i in range (n):
            print(f"{szorzo} * {alap} = {szorzo*alap:2}")
            szorzo+=1
        break
    else:
        print("Negatív számot adtál meg!")
"""
print("\n33. feladat\n")
"""
valasz=1
while True:
    alap=int(input("Alapszám: "))
    n=int(input("Szorzó: "))
    eredmeny=alap*n
    while True:
        if alap==0 or n==0:
            print("A számoknak pozitívnak kell lenniük!")
            break
        valasz=int(input(f"{alap}*{n}="))
        if valasz==eredmeny:
            print("Helyes!")
            break
        elif valasz==0:
            break
        else:
            print("Nem jó!")
    if valasz==0:
        break
"""
print("\n34. feladat\n")
"""
operator = ["+", "-", "*"]
kerdes=10
while kerdes>0:
    muvelet=random.choice(operator)
    szam1=random.randint(1,10)
    szam2=random.randint(1,10)
    while True:
        if muvelet=="+":
            eredmeny=szam1+szam2
        elif muvelet=="-":
            eredmeny=szam1-szam2
        elif muvelet=="*":
            eredmeny=szam1*szam2
        valasz=int(input(f"{szam1}{muvelet}{szam2}= "))
        if valasz==eredmeny:
            print("Helyes!")
            kerdes-=1

            break
        else:
            print("Nem jó!")
"""
print("\n35. feladat\n")
"""
elso = int(input("Első elem: "))
diff = int(input("Differencia: "))
n = int(input("Elemszám: "))
osszeg=0
szam = elso
for i in range (n):
    print(szam, end=", ")
    osszeg+=szam
    szam+=diff
print()
print(osszeg)
"""
print("\n36. feladat\n")
"""
elso = int(input("Első elem: "))
q = int(input("q: "))
n = int(input("Elemszám: "))
osszeg=0
szam = elso
for i in range (n):
    print(szam, end=", ")
    osszeg+=szam
    szam*=q
print()
print(osszeg)
"""
print("\n37. feladat\n")
"""
def lnko(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
 
def lkkt(a, b):
    o = lnko(a, b)
    return a * b // o

szamlalo1=int(input("Számláló1: "))
nevezo1=int(input("Nevező1: "))
szamlalo2=int(input("Számláló2: "))
nevezo2=int(input("Nevező2: "))
a=nevezo1
b=nevezo2
nevezoE=lkkt(a, b)
szamlaloE=nevezoE//nevezo1*szamlalo1+nevezoE//nevezo2*szamlalo2
print(f"{szamlalo1}/{nevezo1}+{szamlalo2}/{nevezo2}={szamlaloE}/{nevezoE}", end="=")
oszto=(max(szamlaloE, nevezoE))
oszto!=0
while True:
    if szamlaloE%10==0 and nevezoE%10==0:
        szamlaloE//=10
        nevezoE//=10
    elif szamlaloE%7==0 and nevezoE%7==0:
        szamlaloE//=7
        nevezoE//=7
    elif szamlaloE%5==0 and nevezoE%5==0:
        szamlaloE//=5
        nevezoE//=5
    elif szamlaloE%3==0 and nevezoE%3==0:
        szamlaloE//=3
        nevezoE//=3
    elif szamlaloE%2==0 and nevezoE%2==0:
        szamlaloE//=2
        nevezoE//=2
    else:
        break
print(f"{szamlaloE}/{nevezoE}")
"""