class Device:
    nev=""

    def __init__(self, nev, allapot) -> None:
        self.nev=nev
        self.allapot=allapot

    def __str__(self) -> str:
        return f"{self.nev} {self.allapot}" 
    
eszkozok=[]
def peldanyositas():
    eszkozok.append(Device("PC1", 0))
    eszkozok.append(Device("PC2", 0))
    eszkozok.append(Device("PC3", 0))

def kapcsolas():
    found=0
    for item in eszkozok:
        if item.allapot==0:
            kapcs="kikapcsolva"
        if item.allapot==1:
            kapcs="bekapcsolva"
        print (f"{item.nev}, {kapcs}")
    melyik=str(input("\nMelyik eszközt kapcsoljuk be?"))
    for item in eszkozok:
        if item.nev==melyik:
            found+=1
            if item.allapot==0:
                item.allapot=1
                print(f"{item.nev} eszközt bekapcsoltuk.")
            else:
                print(f"{item.neve} eszköz már be van kapcsolva.")
    if found==0:
        print("Nincs ilyen nevű eszköz!")
    print()
    for item in eszkozok:
        if item.allapot==0:
            kapcs="kikapcsolva"
        if item.allapot==1:
            kapcs="bekapcsolva"
        print (f"{item.nev}, {kapcs}")

def main():
    peldanyositas()
    kapcsolas()

main()