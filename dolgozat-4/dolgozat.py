def fel1():
    nev=str(input("\nKérem a gyógynövény nevét:"))
    jav=int(input("Kérem a napi szükséges mennyiséget grammban: "))
    eleg=100//jav
    print(f"A(z) {nev} összesen {eleg} napra elegendő")
    if eleg>=30:
        print("Elegendő 30 napra egy dobozzal.")
    else:
        print("Nem elegendő 30 napra egy dobozzal.")

def fel2Beolvasas():
    tarolo=[]
    f=open("novenyek.txt", encoding="UTF-8")
    for item in f:
        szo=item.strip()
        tarolo.append(szo.lower())
    return tarolo
    
def fel2Kiiratasok(tarolo):
    for item in tarolo:
        print(item)
    print(f"\nA gyógynövények száma: {len(tarolo)}\n")

def fel2Kereses(tarolo):
    keresni=str(input("Kérem adjon meg egy nevet: "))
    if keresni in tarolo:
        print("Szerepel a listában.\n")
    else:
        print("Nem szerepel a listában.\n")

def fel2Maganh(tarolo):
    maganhangzok=["a", "é", "á", "ű", "ö", "ü", "ó", "e", "u", "i", "o", "ő", "ú", "í"]
    maganhangzosok=[]
    for item in tarolo:
        if item[0] in maganhangzok:
            maganhangzosok.append(item)
    print("A magánhangzóval kezdődő növények:")
    for item in maganhangzosok:
        print(f"\t{item}")

def fel2Beturend(tarolo):
    abc=sorted(tarolo)
    print("")
    for item in abc:
        print(item)

def fel2():
    tarolo=fel2Beolvasas()
    fel2Kiiratasok(tarolo)
    fel2Kereses(tarolo)
    fel2Maganh(tarolo)
    fel2Beturend(tarolo)

def beolvasas2():
    tarolo=[]

    class Gyogynoveny:
        nev=""
        resz=""
        honapKezd=0
        honapVeg=0
    
        def __init__(self, nev, resz, honapKezd, honapVeg) -> None:
            self.nev=nev
            self.resz=resz
            self.honapKezd=honapKezd
            self.honapVeg=honapVeg

        def __str__(self) -> str:
            return f"{self.nev} {self.resz} {self.honapKezd} {self.honapVeg}"
        
    f=open("gyogynovenyek.txt", encoding="UTF-8")
    f.readline
    for sor in f:
        reszek=sor.strip().split(";")
        nev=reszek[0]
        resz=reszek[1]
        honapKezd=int(reszek[2])
        honapVeg=int(reszek[3])
        tarolo.append(Gyogynoveny(nev, resz, honapKezd, honapVeg))
    return tarolo


def fel3Kiiratasok(tarolo):
    for item in tarolo:
        if item.nev=="Gyongyvirag":
            keres=item.resz
    print(f"A gyöngvirág {keres} részét gyűjtik.")

    leveles=0
    for item in tarolo:
        if item.resz=="level":
            leveles+=1
    print(f"{leveles} növényt gyűjtenek a leveléért.\n")

    reszek=[]
    for item in tarolo:
        if item.resz not in reszek:
            reszek.append(item.resz)
    print("A virágok gyűjtött részei:")
    for item in reszek:
        print(f"\t{item}")

    osszel=[]
    for item in tarolo:
        if item.honapKezd==9 or item.honapKezd==10 or item.honapKezd==11:
            osszel.append(item)
    print(f"\nEzeket a növényeket kezdik gyűjteni ősszel:")
    for item in osszel:
        print(f"\t{item.nev}")
    
    viragaert=0
    for item in tarolo:
        if item.resz=="virag" or item.resz=="viragzat" or item.resz=="viragzo hajtas":
            viragaert+=1
    print(f"\n{viragaert} növényt gyűjtenek a virágáért.\n")

def extra1(tarolo):
    for item in tarolo:
        honapok=item.honapVeg-item.honapKezd
        print(f" A(z) {item.nev} növényt {abs(honapok)} hónapig gyűjtik.")

def extra2(tarolo):
    gyujtenek=[]
    for item in tarolo:
        szam=12
        while szam>0:
            if szam==item.honapVeg:
                szam-=1
                

def fel3():
    tarolo=beolvasas2()
    fel3Kiiratasok(tarolo)
    extra1(tarolo)
    

def main():
    print("1. feladat")
    fel1()
    print("\n2. feladat\n")
    fel2()
    print("\n3. feladat\n")
    fel3()    

main()