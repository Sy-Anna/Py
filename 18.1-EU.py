import datetime

class Csatlakozas:
    def __init__(self, orszag, datum) -> None:
        self.orszag=orszag
        self.datum=datum
    def __str__(self) -> str:
        return f"{self.orszag} {self.datum.date()}"


#globalis
lista=[]

def beolvas():
    f = open("eucsatlakozas.txt", encoding="UTF-8")
    for item in f:
        reszek = item.strip().split(';')
        orszag=reszek[0]
        format="%Y.%m.%d"
        datum = datetime.datetime.strptime(reszek[1], format)   
        lista.append(Csatlakozas(orszag, datum))

    for item in lista:
        print(item)

def feladat3():
    print(f"3. feladat")
    print(f"{len(lista)} tagállama van az uniónak.")
    print()

def feladat4():
    print("4. feladat")
    het=[]
    szam=0
    segedlista=[item for item in lista if item.datum.year==2007]        #eyszerüsitett for
    for item in lista:                  #<-- sima forral
        if item.datum.year == 2007:
            het.append(item)                #<--
    print("2007-ben csatlakozott tagállamok:")
    for item in segedlista:
        print(item)
    print(f"{len(segedlista)} ország csatlakozott 2007-ben.")
    print()
    

def feladat5():
    print("5. feladat")
    segedlista=[item for item in lista if item.orszag == "Magyarország"][0]
    print(f"Magyarország {segedlista.datum.date()}-ban csatlakozott egyszerűsített for-ral.")
    for item in lista:
        if item.orszag == "Magyarország":
            ev = (item.datum.year)
    print(f"Magyarország {ev}-ben csatlakozott az EU-hoz.")
    print()

def feladat6():
    print("6. feladat")
    seged=len([item for item in lista if item.datum.month ==5])
    if seged==0:
        print("Nem volt májusban csatlakozás.")
    else:
        print (f"{seged} ország csatlakozott májusban.")
        print("A csatlakozott országok:")
    print()

def fel7():
    print("7. feladat")
    maxi=lista[0] #objektum: mindent is tárolok róla
    for item in lista:
        if item.datum > maxi.datum:
            maxi=item
    print(f"Legutoljára {maxi.orszag} csatlakozott.")
    print()

def f8():
    print("8. feladat")
    # kulcs: csatlakozás éve
    #érték: adott évben hány ország csatlakozott
    stat={}
    for item in lista:
        kulcs=item.datum.year
        if kulcs not in stat: #ha még nincs ilyen kulcsa a statban
            stat[kulcs]=0   #nulla kezdőértékkel létrehozom
        stat[kulcs]+=1

    for kulcs in stat:
        print(f"{kulcs}-{stat[kulcs]}")


def main():
    beolvas()
    print("1-2 feladat")
    print()
    d = datetime.datetime.now()
    print (d)
    d1 = datetime.datetime(2023,11,30)
    print(d1.year == d.year and d1.month == d.month)
    print()
    feladat3()
    feladat4()
    feladat5()
    feladat6()
    fel7()
    f8()
    



main()