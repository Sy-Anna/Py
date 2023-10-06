import random
import math

print(" ")
print("8. feladat")
print(" ")
#n = int(input("n ="))
#szam = 1
#for i in range (n):
#    print (szam*szam, end=" ")
#    szam = szam+1
print(" ")
print("9. feladat")
print(" ")
#n = int(input("n ="))
#for i in range(1, n, 2):
#    print(i, end=" ")
print(" ")
print("10. feladat")
print(" ")
#k = int(input("k= "))
#szam1 = 1
#szam2 = 2
#for i in range (k-1):
#    print (f"{szam1}*{szam2}+", end="")
#    szam1 = szam1+1
#    szam2 = szam2+1
#print(f"{k}*{k+1}")
print(" ")
print("11. feladat")
print(" ")
#n = int(input("n= "))
#szorzo = 1
#for i in range (n):
#    if 3*szorzo <= n:
#        print(3*szorzo, end= " ")
#    szorzo = szorzo+1
print(" ")
print("12. feladat")
print(" ")
"""
szam1 = 0
szam2 = 1
n = int(input("n= "))
print(f"{szam1}, {szam2}", end=", ")
for i in range (n-2):
    eredmeny = szam1 + szam2
    print(f"{eredmeny}", end=", ")
    szam1 = szam2
    szam2 = eredmeny
"""
print(" ")
print("13. feladat")
print(" ")
"""
def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list
 
starting_range = 1
ending_range = int(input("n= "))
lst = prime(starting_range, ending_range)
if len(lst) == 0:
    print("")
else:
    print("prímek: ", lst)
""" #lopott
print(" ")
print("14. feladat")
print(" ")
"""
n = int(input("n= "))
print(" ")
kezdo = 0
print (f" * |", end=" ")
for i in range(n):
    kezdo += 1
    print (f"{kezdo:4}", end="")
print()
for i in range (n*3+5):
    print("=", end="")
print()
kezdo = 0
szorzat = 1
for i in range(n):
    kezdo += 1
    print (f"{kezdo:2}", "|", end=" " )
    for j in range (n):
        print(f"{szorzat:3}", end=" ")
        szorzat += 1
    print()
"""
print(" ")
print("15. feladat")
print(" ")
"""
szam1 = random.randint (0,10)
szam2 = random.randint (0,25)
szam3 = random.randint (0,50)
szam4 = random.randint (10,75)
szam5 = random.randint (-50,50)
szam6 = random.randint (-100,-70)
szam7 = random.randint (0,25)
szam8 = random.randint (-50,50)
szam9 = random.randint (-100,-70)
szam10 = random.randint (10,75)
print(f"{szam1}, {szam2}, {szam3}, {szam4}, {szam5}, {szam6}, {szam7}, {szam8}, {szam9}, {szam10}")
"""
print(" ")
print("16. feladat")
print(" ")
print(" ")

"""n = int(input("n= "))
for i in range (n):
    print("*", end="")
print()
for i in range (4):
    print("*", end="")
    for j in range (n-2):
        print(" ", end="")
    print("*")
for i in range (n):
    print("*", end="")"""

print(" ")
print("17. feladat")
print(" ")
"""n = int(input("n= "))
m = int(input("m= "))
print("")
for i in range (n):
    print("*", end="")
print()
for i in range (m-2):
    print("*", end="")
    for j in range (n-2):
        print(" ", end="")
    print("*")
for i in range (n):
    print("*", end="")
print()"""
print(" ")
print("18. feladat")
print(" ")
n = int(input("n= "))
m = int(input("m= "))
print("")
x = m/2
for i in range (x):
    print(" ", end="")
for i in range (n):
    print("*", end="")
print()
for i in range (m-2):
    print("*", end="")
    for j in range (n-2):
        print(" ", end="")
    print("*")
for i in range (n):
    print("*", end="")
print()  #nem jó

"""n = int(input("n= "))
m = int(input("m= "))

for i in range (m):
    x = math.ceil(m/2)
    for j in range (x):
        print("x", end="")
        x = x-1
        for k in range (n):
            print("*", end="")
        print()"""  #katasztrofa

print(" ")
print("19. feladat")
print(" ")

#tudni kéne hozzá az előzőt

print(" ")
print("20. feladat")
print(" ")

"""n = int(input("n= "))
m = int(input("m= "))
for i in range (n):
    print("*", end="")
print()
for i in range (m-2):
    print("*", end="")
    for j in range (n-2):
        print(" ", end="")
    print("*")
for i in range (n):
    print("*", end="")"""

print(" ")
print("21. feladat")
print(" ")

"""x = random.randint (1, 100)
y = random.randint (1, 100)
print(f"x={x}, y={y}")
osszeg = int(input("Összegük= "))
kulonbseg = int(input("Különbségük ="))
if osszeg == x+y:
    print("Az összegük helyes!")
else:
    print(f"Nem jó! A helyes összeg {x+y}")
if kulonbseg == x-y:
    print("A különsgégük helyes!")
else:
    print(f"Nem jó! A helyes különbség {x-y}")"""

print(" ")
print("22. feladat")
print(" ")
print("Kód\tKarakter")
"""
for i in range (32, 256, 1):
    print(f"{i:3}\t{chr(i)}")
    print()
"""
print(" ")
print("23. feladat")
print(" ")
"""
szam = int(input("Adjon meg egy számot: "))
for i in range (1, szam):
    if szam % i == 0:
        print(i, end=", ")
"""
print()
print(" ")
print("24. feladat")
print(" ")
"""
szam = int(input("Adjon meg egy számot: "))
x = 0
for i in range (1, szam+1):
    if szam % i == 0:
        x += i
print(f"A szám osztóinak összege = {x}")
"""
print("")
print("25. feladat")
print(" ")
"""
n = int(input("n= "))
x = 0
y = 0
for i in range (1, n):
    if n % i == 0:
        x=i
        y+=i
        print(x, end="+")
print(n)
print()
y+=n
if y == n*2:
    print(f"2*{n}={y}, ez egy tökéletes szám!")
else:
    print(f"2*{n} nem egyenlő {y}, ez nem tökéletes szám!")
"""
print("")
print("26. feladat")
print("")
"""
alap = int(input("hatványalap: "))
kitevo = int(input("hatványkitevő: "))
ertek = alap**kitevo
print(f"A hatványérték {ertek}")
"""
print(" ")
print("27. feladat")
print(" ")
