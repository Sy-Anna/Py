import random

def fel1():
    nev=str(input("Játékos neve: "))
    kartya=str(input("piros vagy fekete kártya?"))
    szinek=["piros", "fekete"]
    generalt=random.choice(szinek)
    if generalt==kartya:
        print("Gratulálok, nyertél!")
    else:
        print("Sajnálom, vesztettél!")


def fel2():
    class OrszagVaros:
        orszag=""
        varos=""

        def __init__(self, orszag, varos) -> None:
            self.orszag=orszag
            self.varos=varos

        def __str__(self) -> str:
            return f"{self.orszag} {self.varos}"
        
    tarolo=[]
    tarolo.append(OrszagVaros("Magyarország", "Budapest"))
    tarolo.append(OrszagVaros("Franciaország", "Párizs"))
    tarolo.append(OrszagVaros("Kanada", "Torontó"))

    valasz=str(input("Adjon meg egy országot: "))
    talalt=False
    szam=len(tarolo)
    while talalt==False or szam>0:
        for item in tarolo:
            if item.orszag==valasz:
                print(f"Az ország fővárosa: {item.varos}")
                talalt=True
            szam-=1
        

def fel3():
    class Hallgato:
        nev=""
        szul_ev=0
        szak=""

        def __init__(self,szul_ev, nev, szak) -> None:
            self.nev=nev
            self.szul_ev=szul_ev
            self.szak=szak
        
        def __str__(self) -> str:
            return f"{self.nev} {self.szul_ev} {self.szak}"
    egyetemistak=[]
    f=open("egyetemistak.txt", encoding="UTF-8")
    for item in f:
        resz=item.strip().split(";")
        nev=resz[0]
        ev=resz[1]
        szak=resz[2]
        egyetemistak.append(Hallgato(nev, ev, szak))

    for item in egyetemistak:
        print(item.nev)
        valasz=str(input("Kíván hozzáadni hallgatót? i/n "))
        if valasz=="i":
            while True:
                uj_nev=str(input("Az új hallgató neve: "))
                for item in egyetemistak:
                    if item.nev==uj_nev:
                        print("Az egyetemista már rajta van a listán.")
                        break
                uj_ev=str(input("Az új hallgató születési éve: "))
                uj_szak=str(input("Az új hallgató szaka: "))
                uj_hallgato=(Hallgato(uj_nev, uj_ev, uj_szak))
                egyetemistak.append(uj_hallgato)
                print("Az új hallgató még nem volt rajta a listán, hozzáadásra került.")
                valasz2=str(input("Hozzá kíván még adni hallgatót a listához?"))
                if valasz2=="n":
                    break
        valasz=str(input("kíván eltávolítani hallgatót a listáról? i/n "))
        if valasz=="i":
            while True:
                found=False
                uj_nev=str(input("Az eltávolítandó hallgató neve: "))
                for item in egyetemistak:
                    if item.nev==uj_nev:
                        egyetemistak.remove(item)
                        print("Az illetőt eltávolítottuk a listáól.")
                        found==True
                if found==False:
                    print("A hallgató nem volt rajta a listán.")
                valasz2=str(input("El kíván még távolítani hallgatót a listáról?"))
                if valasz2=="n":
                    break

def main():
    fel3()

main()