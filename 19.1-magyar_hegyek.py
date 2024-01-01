class Hegyek:
    nev=""
    hegyseg=""
    magassag=0

    def __init__(self, nev, hegyseg, magassag) -> None:
        self.nev=nev
        self.hegyseg=hegyseg
        self.magassag=magassag
        
    def __str__(self) -> str:
        return f"{self.nev} {self.hegyseg} {self.magassag}"

hegyek=[]
def beolvasas():        
    f = open('hegyekMO.txt', encoding="UTF-8")
    f.readline()
    for sor in f:
        szavak=sor.strip().split(';')
        nev=szavak[0]
        hegyseg=szavak[1]
        magassag=int(szavak[2])
        hegyek.append(Hegyek(nev, hegyseg, magassag))

def fel3():
    print("3. eladat")
    print(f"{len(hegyek)} hegy van a listában.")

def fel4():
    print("\n4. feladat")
    mag=0
    for item in hegyek:
        mag+=item.magassag
    atlag=mag/len(hegyek)
    print(f"Átlagosan {atlag} méter magasak a hegyek magyarországon.")

def fel5():
    print("\n5. feladat")
    max=hegyek[0]
    for item in hegyek:
        if item.magassag>max.magassag:
            max=item
    print(f"A legmagasabb hegycsúcs adatai:\nNév: {max.nev}\nHegység: {max.hegyseg}\nMagasság: {max.magassag} m")

def fel6():
    print("\n6. feladat")
    kereses=int(input("Adjon meg egy magasságot: "))
    found=0
    while found==0:
        for item in hegyek:
            if item.magassag>kereses and item.hegyseg=="Börzsöny":
                found+=1
                print(f"Van a megadott magasságnál magasabb hegy a Börzsönyben.")
                break
        if found == 0:
            print("Nincs a megadott magasságnál magasabb hegy a Börzsönyben.")
            break

def fel7():
    print("\n7. feladat")
    meter=3000/3.280839895
    szam=0
    for item in hegyek:
        if item.magassag>meter:
            szam+=1
    print(f"A 3000 lábnál magasabb hegyek száma: {szam}")

def fel8():
    matra=0
    bukk=0
    borzsony=0
    zemplen=0
    koszeg=0
    for item in hegyek:
        if item.hegyseg=="Mátra":
            matra+=1
        elif item.hegyseg=="Bükk-vidék":
            bukk+=1
        elif item.hegyseg=="Börzsöny":
            borzsony+=1
        elif item.hegyseg=="Zempléni-hegység":
            zemplen+=1
        elif item.hegyseg=="Kőszegi-hegység":
            koszeg+=1
    print(f"\n8. feladat")
    print(f"Hegységek statisztika\nMátra - {matra} db\nBükk-vidék - {bukk} db\nBörzsöny - {borzsony} db\nZempléni - {zemplen} db\nKőszegi - {koszeg} db")


def main():
    beolvasas()
    fel3()
    fel4()
    fel5()
    fel6()
    fel7()
    fel8()


main()