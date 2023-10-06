print("")
print("4. feladat")
print("")

"""
szam = int(input("szám: "))
osszeg=szam
print(osszeg)
while True:
    szam = int(input("szám: "))
    if szam > 0 or szam < 0:
        osszeg*=szam
        print(osszeg)
    if szam == 0:
        break
    print(osszeg)
"""

print(" ")
print("5. feladat")
print(" ")

"""
karakter = input("karakter: ")
szam = int(input("szám: "))
for i in range (szam):
    print(karakter, end="")
"""

print("")
print("6. feladat")
print("")

"""
szam1 = int(input("szam1: "))
szam2 = int(input("szam2: "))
print(min(szam1, szam2), max(szam1, szam2))
"""


print("")
print("8. feladat")
print("")

"""
for i in range (1000):
    if i%3==0 and i%5==0:
        print(i, end=", ")
"""

print("")
print("9. feladat")
print("")

"""
osszeg = int(input("összeg= "))
osszeg = round(osszeg, 2)
maradek = osszeg
while maradek>5:
    ketsz = 0
    egysz = 0
    otven = 0
    huszas = 0
    tizes = 0
    otos = 0
    if osszeg < 1 or osszeg > 1000:
        print("nem jó összeg!")
        break
    if maradek/200 > 0:
        db = maradek//200
        maradek = maradek%200
        if db>0:
            print(f"{db}db kétszázas")
    if maradek/100 > 0:
        db = maradek//100
        maradek = maradek%100
        if db>0:
            print(f"{db}db százas")
    if maradek/50 > 0:
        db = maradek//50
        maradek = maradek%50
        if db>0:
            print(f"{db}db ötvenes")
    if maradek/20 > 0:
        db = maradek//20
        maradek = maradek%20
        if db>0:
            print(f"{db}db huszas")
    if maradek/10 > 0:
        db = maradek//10
        maradek = maradek%10
        if db>0:
            print(f"{db}db tízes")
    if maradek/5 > 0:
        db = maradek//5
        maradek = maradek%5
        if db>0:
            print(f"{db}db ötös")
    if maradek == 0:
        break
"""

print("")
print("vagy")
print("")


osszeg = int(input("összeg= "))
cimlet = 200
while osszeg>5:
    db = osszeg//cimlet
    if db >= 1:
        print(f"{cimlet}Ft: {db} db szükséges")
    osszeg%=cimlet
    if cimlet == 200:
        címlet = 100
    elif cimlet == 100:
        címlet = 50
    elif címlet == 50:
        címlet = 20
    elif címlet == 20:
        címlet = 10
    elif címlet == 10:
        címlet = 5
