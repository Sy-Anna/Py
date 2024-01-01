import datetime

class Pilota:
    neve=""
    szuletett=""
    nemzetiseg=""
    rajtszam=0

    def __init__(self, neve,  szuletett, nemzetiseg, rajtszam) -> None:
        self.neve=neve
        self.szuletett=szuletett
        self.nemzetiseg=nemzetiseg
        self.rajtszam=rajtszam

    def __str__(self) -> str:
        return f"{self.neve} {self.szuletett.date()} {self.nemzetiseg} {self.rajtszam}"

pilotak=[]
        


def beolvasas():
    f = open("pilotak.csv", encoding="UTF-8")           #f==mutató - biztosítja az elérhetőségét a file-nak
    f.readline()                                        #első sort beolvasta, második sor elején várakozik
    for sor in f:
        szavak = sor.strip().split(';')
        neve=szavak[0]
        format="%Y.%m.%d"
        szuletett=datetime.datetime.strptime(szavak[1], format)
        nemzetiseg=szavak[2]
        rajtszam=szavak[3]
        pilotak.append(Pilota(neve, szuletett, nemzetiseg, rajtszam)) 

def fel1():
    print("3. feladat")
    print(f"{len(pilotak)} pilóta van az adatállományban.")
    print()

def fel2():
    print("4. feladat")
    ossz=len(pilotak)
    utolso=pilotak[ossz-1]
    print(f"{utolso.neve} Az utolsó pilóta az állományban.")
    print()


def fel3():
    print("5. feladat")
    seged=[]
    for item in pilotak:
        if item.szuletett.year < 1901:
            seged.append(item)
            print(item.neve, item.szuletett)
    print()

def fel4():
    print("6. feladat")
    min=pilotak[0]
    for item in pilotak:
        if item.rajtszam != "" :
            if item.rajtszam < min.rajtszam:
                min=item
    print(f"A legkisebb rajtszámú versenyző {min.nemzetiseg}")
    print()

def fel5():
    pass
    

def main():
    beolvasas()
    fel1()
    fel2()
    fel3()
    fel4()

main()

"""for item in pilotak:
    print(item)"""
