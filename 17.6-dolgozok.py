class Employee:
    nev=""
    poz=""
    fiz=0

    def __init__(self, nev, poz, fiz) -> None:
        self.nev=nev
        self.poz=poz
        self.fiz=fiz

    def __str__(self) -> str:
        return f"{self.nev} {self.poz}"
    
dolgozok=[]
def peldanyositas():
    dolgozok.append(Employee("Kiss Béla", "ásó", 234987))
    dolgozok.append(Employee("Kiss Béláné", "kapa", 987543))
    dolgozok.append(Employee("Ifj. Kiss Béláné", "nagyharang", 0))

def emeles():
    for item in dolgozok:
        print(f"{item.nev} dolgozó {item.poz} pozicióban {item.fiz} Ft-ot keres.")
    kinek=str(input("Kinek emeljük a fizetését? "))
    mennyivel=int(input("Mennyivel emeljük?"))
    found=0
    for item in dolgozok:
        if kinek==item.nev:
            found+=1
            item.fiz+=mennyivel
            print(f"{item.nev} dolgozó {item.poz} pozicióban mostmár {item.fiz} Ft-ot keres.\n")
    if found==0:
        print("Nincs ilyen dolgozónk!")

def main():
    peldanyositas()
    emeles()

main()