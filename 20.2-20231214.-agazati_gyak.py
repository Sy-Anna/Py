class Snooker:
    ranglista=0
    nev=""
    orszag=""
    osszeg=0

    def __init__(self, ranglista, nev, orszag, osszeg) -> None:
        self.ranglista=ranglista
        self.nev=nev
        self.orszag=orszag
        self.osszeg=osszeg

    def __str__(self) -> str:
        return f"{self.ranglista} {self.nev} {self.orszag} {self.osszeg}"

lista=[]

def beolvasas():
    f=open('snooker 1.txt', encoding='UTF_8')
    f.readline()
    for sor in f:
        reszek=sor.strip().split(";")
        ranglista=int(reszek[0])
        nev=reszek[1]
        orszag=reszek[2]
        osszeg=int(reszek[3])
        lista.append(Snooker(ranglista, nev, orszag, osszeg))


def fel3():
    print(f"3. feladat: A vilégranglistán {len(lista)} versenyző szerepel")

def fel4():
    osszesen=0
    for item in lista:
        osszesen+=item.osszeg
    atlag=osszesen/len(lista)
    print(f"4. feladat: A versenyzők átlagosan {atlag:.2f} forintot kerestek")

def fel5():
    max=lista[0]
    for item in lista:
        if item.orszag=="Kína":
            if item.osszeg<max.osszeg:
                max=item
    forintban=max.osszeg*380
    print(f"5. feladat: A legjobban kereső kínai versenyző:\n\tHelyezés: {max.ranglista}\n\tNév: {max.nev}\n\tOrszág: {max.orszag}\n\tNyeremény összege: {forintban} Ft")

def fel6():
    talalt=0
    for item in lista:
        if item.orszag=="Norvégia":
            talalt+=1
    if talalt==0:
        print("6. feladat: A versenyzők között nincs norvég versenyző.")
    else:
        print("6. feladat: A versenyzők között van norvég versenyző.")

def fel7():
    print("7. feadat: Statisztika")
    orszagok=[]
    for item in lista:
        if item.orszag not in orszagok:
            orszagok.append(item.orszag)
    szam=0
    while szam<=len(orszagok)-1:
        seged=[]
        for item in lista:
            if item.orszag==orszagok[szam]:
                seged.append(item)
        if len(seged)>4:
            print(f"\t{orszagok[szam]} - {len(seged)} fő")
        szam+=1

            

def main():
    beolvasas()
    fel3()
    fel4()
    fel5()
    fel6()
    fel7()

main()