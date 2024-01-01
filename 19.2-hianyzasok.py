
class Hianyzas:
    def __init__(self, nev, osztaly, elso, utolso, mulasztott) -> None:
        self.nev=nev
        self.osztaly=osztaly
        self.elso=elso
        self.utolso=utolso
        self.mulasztott=mulasztott

    def __str__(self) -> str:
        return f"{self.nev} {self.osztaly} {self.elso} {self.utolso} {self.mulasztott}"

hianyzasok=[]
def beolvasas():        #1. feladat
    f=open("szeptember.csv")
    f.readline()
    for sor in f:
        szavak=sor.strip().split(";")
        nev=szavak[0]
        osztaly=szavak[1]
        elso=int(szavak[2])
        utolso=int(szavak[3])
        mulasztott=int(szavak[4])
        hianyzasok.append(Hianyzas(nev, osztaly, elso, utolso, mulasztott))

def fel2():
    mulasztas=0
    for item in hianyzasok:
        mulasztas+=item.mulasztott
    print(f"2. feladat\n Az összes mulasztott órák száma: {mulasztas}")

def fel3():
    print("3-4. feladat")
    nap=int(input("Adjon meg egy napot 1. és 30. között: "))
    tanulo=str(input("Adja meg egy tanuló nevét: "))
    found=0
    for item in hianyzasok:
        if tanulo==item.nev:
            found+=1
            if item.mulasztott>0:
                print("A tanuló hiányzott az adott napon.")
            else:
                print("A tanulónak nincs hiányzása.")
        elif found==0:
                print("A tanulónak nincs hiányzása.")
    return tanulo, nap
                
def fel5():
    nap=0
    print("5. feladat:\nAz előző feladatban bekért napon hiányzottak:")
    for item in hianyzasok:
        if item.elso==nap or item.utolso==nap:
            print(item)

def fel6():
    pass

def main():
    beolvasas()
    fel2()
    fel3()
    fel5()
    fel6()

main()