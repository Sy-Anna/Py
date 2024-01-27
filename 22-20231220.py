import math

class VB:
    varos=""
    stadion=""
    stadionALT=""
    ferohely=0
    def __init__(self, varos, stadion, stadionALT, ferohely):
        self.varos=varos
        self.stadion=stadion
        self.stadionALT=stadionALT
        self.ferohely=ferohely
    def __str__(self) -> str:
        return f"{self.varos} {self.stadion} {self.stadionALT} {self.ferohely}"       

lista=[]
def beolvasas():
    f=open('vb2018.txt', encoding='ANSI')
    f.readline()
    for sor in f:
        reszek=sor.strip().split(";")
        varos=reszek[0]
        stadion=reszek[1]
        stadionALT=reszek[2]
        ferohely=int(reszek[3])
        lista.append(VB(varos, stadion, stadionALT, ferohely))

def fel3():
    szam=len(lista)
    print(f"3. feladat: Stadionok száma: {szam}")

def fel4():
    min=lista[0]
    for item in lista:
        if item.ferohely<min.ferohely:
            min=item
    print(f"4. feladat: A legkevesebb férőhely:\n\tVáros: {min.varos}\n\tStadion neve: {min.stadion}\n\tFérőhely: {min.ferohely}")

def fel5():
    osszeg=0
    for item in lista:
        osszeg+=item.ferohely
    atlag1=osszeg//len(lista)
    atlag2=math.floor((osszeg/len(lista)-math.floor(atlag1))*10)
    print(f"5. feladat: Átlagos férőhelyszám: {atlag1},{atlag2}")

def fel6():
    seged=[]
    for item in lista:
        if item.stadionALT!="n.a.":
            seged.append(item)
    print(f"6. feladat: Két néven is ismert stadionok száma: {len(seged)}")

def fel7():
    while True:
        kereses=str(input("7. feladat: Kéérem a város nevét: "))
        if len(kereses)>=3:
            break
    found=0
    while found==0:
        for item in lista:
            if item.varos==kereses:
                found+=1
        break
    return found

def fel8(found):
    if found==0:
        print("8. feladat: A megadott város nem VB helyszín.")
    else:
        print("8. feladat: A megadott város VB helyszín.")

def fel9():
    seged=[]
    for item in lista:
        if item.varos not in seged:
            seged.append(item.varos)
    print(f"9. feladat: {len(seged)} különböző városban voltak mérkőzések.")

def main():
    beolvasas()
    fel3()
    fel4()
    fel5()
    fel6()
    found=fel7()
    fel8(found)
    fel9()
main()