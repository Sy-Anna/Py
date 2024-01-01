import random
'''
kazmer = [3,"BMW", 23.5, "Ázsia", "sör"]
print(len(kazmer))
print(kazmer)
print(kazmer[0])
kazmer[0]="Feri"
print(kazmer[0])
del(kazmer[0])
print(kazmer)
kontinesek=["európa","ázsia"]
print(kontinesek)
kontinesek.append("amerika")
print(kontinesek)
kontinesek.insert(1,"ausztrália")
print(kontinesek)
print(kontinesek.index("európa"))
kontinesek.sort()
print(kontinesek)
import locale
locale.setlocale(locale.LC_ALL,"HU_hu.UTF8")
kontinesek.sort()
print(kontinesek)
kontinesek.pop(kontinesek.index("ázsia"))
print(kontinesek)
masolat=kontinesek.copy()
print(masolat)

'''


def fel1():
    lista=[]
    for i in range (10):
        lista.append(random.randint(5,10))
    print(lista1)

def fel2():
    ertek=["Igaz", "Hamis"]
    lista=[]
    for i in range(15):
        lista.append(random.choice(ertek))
    print(lista)

def fel3(): #nem jó
    lista=[1, 2, 3, 4, 5,6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    paratlan=[]
    szam=1
    print(len(lista))
    hanyszor=len(lista)
    for i in range (hanyszor):
        if (lista[szam])%2==0:
            paratlan.append(lista[szam])
        szam+=1
    szam=0
    hanyszor=len(paratlan)
    for i in range (hanyszor):
        negyzet=paratlan[szam]**2
        print(negyzet, end=", ")
        szam+=1
    print()
        
def fel4():
    lista=[]
    for i in range (5):
        lista.append(int(input("Adjon meg egy számot:")))
    print(lista)
    lista.reverse()
    print(lista)
    lista.reverse()
    valtozo=1
    for i in range (len(lista)):
        if valtozo%2==0:
            print(lista[valtozo-1], end=" ")
        valtozo+=1
    print()
    szam=int(input("Adjon meg egy számot 1 és 5 között: "))
    if szam>5 or szam<1:
        szam=int(input("Nem jó, adjon meg egy számot 1 és 5 között: "))
    print(lista[szam-1])

def fel5():
    lista1=[1, 2, 3, 4, 5]
    lista2=[6, 7, 8, 9, 10]
    print(lista1)
    print(lista2)
    lista3=[]
    szam=0
    for i in range (5):
        lista3.append(lista1[szam]+lista2[szam])
        szam+=1
    print(lista3)

def fel6():
    lista=["első", "második", "harmadik", "negyedik", "ötödik"]
    print(lista)
    while True:
        valasz=input("Jobbra vagy balra toljuk? (j/b) ")
        if valasz=="j":
            lista.insert(0, lista[4])
            del(lista[5])
            print(lista)
        elif valasz=="b":
            lista.insert(4, lista[0])
            del(lista[0])
            print(lista)
        elif valasz==0:
            break

def fel7():
    lista=[1, 2, 3, 4, 5]
    print(lista)
    lista.reverse()
    print(lista)

def fel8():
    lista=[]
    while True:
        szam=int(input("Adjon meg egy számot: "))
        if szam%1==0:
            lista.append(szam)
        elif szam==0:
            break
    print(lista)
    hanyszor=len(lista)
    szam=0
    eredmeny=0
    for i in range (hanyszor):
        eredmeny+=lista[szam]
        szam+=1
    print(eredmeny)

def fel9(): #nem értem
    print("asd")

def fel10():
    lista=[]
    while True:
        valasz=int(input("Adjon meg egy számot: "))
        lista.append(valasz)
        if valasz==0:
            break
    print(lista)
    szam=0
    eredmeny=0
    while True:
        if lista[szam]>0 and lista[szam+1]<0:
            eredmeny+=1
        elif lista[szam]==0:
            break
        szam+=1
    print(eredmeny)

def fel11():
    lista=[]
    while True:
        szam=float(input("szám: "))
        lista.append(szam)
        if szam==0:
            break
    szam=0
    kerekitett=[]
    kerekítés=0
    for i in range (len(lista)):
        kerekítés=round(lista[szam], 2)
        kerekitett.append(kerekítés)
        szam+=1
    print(kerekitett)

def fel12(): #nem jó
    lista=[]
    for i in range (20):
        szam=random.randint(-100, 100)
        lista.append(szam)
    print(lista)
    print()
    szam=1
    for i in range (20):
        print(szam, end=". ")
        if lista[szam-1]>=0:
            print("", lista[szam-1], end="  ")
            print("+")
        else:
            print(lista[szam-1], end=" ")
            print(" -")
        szam+=1
        print()
    szam=2
    print(lista)
    kalkulator=0
    kalkulator2=0
    while szam<=20:
        kalkulator=lista[szam]
        kalkulator+=1
        lista[szam]=kalkulator
        szam+=3
    print(lista)
    szam=1
    while szam<=20:
        kalkulator=lista[szam]
        kalkulator2=lista[szam-1]
        lista[szam]=kalkulator-kalkulator2
        szam+=2
    print[lista]

def fel13():
    #elfáradtam
