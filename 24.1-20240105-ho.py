import random

def fel1():
    ar=int(input("Adja meg a termék árát: (Ft) "))
    eladott=int(input("Adja meg az éves eladott mennyiséget: (db)" ))
    atlag_bev=round(ar*eladott/12, 2)
    print(f"A havi átlagbevétel {atlag_bev} Ft.")
    if atlag_bev>35000:
        print("A termék nyereséges.")
    else:
        print("A termék nem volt nyereséges.")

def beolvasas():
    tarolo=[]
    f=open("elemek.txt", encoding="UTF-8")
    for sor in f:
        szo=sor.strip()
        tarolo.append(szo)
    return tarolo

def kereses(lista):
    for item in lista:
        print(item)
    valasz=str(input("A keresett elem: "))
    if valasz in lista:
        print("A keresett elem a listában van.")
    else:
        print("A keresett elem nincs a listában.")
def ajanlas(lista):
    print("Az ajánlott elem:")
    print(random.choice(lista))

def elemek():
    tarolo=beolvasas()
    kereses(tarolo)
    ajanlas(tarolo)
    
def beolvasas2():
    class Korcsolya:
        nev=""
        orszag=""
        technika=""
        komponens=0
        lenonas=0
        
        def __init__(self, nev, orszag, technika, komponens, levonas) -> None:
            self.nev=nev
            self.orszag=orszag
            self.technika=technika
            self.komponens=komponens
            self.levonas=levonas

        def __str__(self) -> str:
            return f"{self.nev} {self.orszag} {self.technika} {self.komponens} {self.levonas}"

    f=open("korcsolya.csv", encoding="UTF-8")
    tarolo=[]
    f.readline()
    for sor in f:
        reszek=sor.strip().split(";")
        nev=reszek[0]
        orszag=reszek[1]
        technika=reszek[2]
        komponens=reszek[3]
        levonas=reszek[4]
        tarolo.append(Korcsolya(nev, orszag, technika, komponens, levonas))
    return tarolo

def kiiartas2(tarolo):
    for item in tarolo:
        print (item)
    print(f"{len(tarolo)} versenyző volt")


def korcsolyazas():
    tarolo=beolvasas2()
    kiiartas2(tarolo)


def main():
    #elemek()
    korcsolyazas()


main()
