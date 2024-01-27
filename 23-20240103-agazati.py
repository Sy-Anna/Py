def fel1():
    ar=int(input("Adja meg az almabor árát Forintban: "))
    db=int(input("Adja meg, hány darab almabort adott el ma: "))
    bevetel=ar*db
    print(f"{bevetel}Ft volt a napi bevétel.")
    if bevetel>10000:
        print("A bevétel meghaladja a 10000Ft-ot.")
    else:
        print("A bevétel nem haladja meg a 10000Ft-ot.")

def fel2():
    versenyzo=str(input("A versenyző neve: "))
    pont1=int(input("A versenyző pontszáma az első feladatrészben: "))
    pont2=int(input("A versenyző pontszáma a második feladatrészben: "))
    osszPont=pont1+pont2
    print(f"{versenyzo} összpontszáma: {osszPont}")
    if osszPont>=70:
        print("Ez elégséges pontszám a nyereményhez.")
    else:
        print("Nem elégséges pontszám a nyereményhez.")

def fel3():
    f=open("asd.txt", encoding="UTF-8")
    lista=[]
    while True:
        for item in f:
            szavak=item.strip().split(" ")
            for szavak in f:
                if len(szavak)>0:
                    lista.append(szavak)
                else:
                    print(f" {len(lista)} szó van a file-ban.")
                    break
        break
    #nem jó

def fel4():
    class Indian():
        nev=""
        nem=""
        kor=0
        tulaj=""

        def __init__(self, nev, nem, kor, tulaj) -> None:
            self.nev=nev
            self.nem=nem
            self.kor=kor
            self.tulaj=tulaj

        def __str__(self) -> str:
            return f"{self.nev} {self.nem} {self.kor} {self.tulaj}"
        
    f=open("indian.txt", encoding="UTF-8")
    indianok=[]
    for sor in f:
        reszek=sor.strip().split(",")
        nev=reszek[0]
        nem=reszek[1]
        kor=int(reszek[2])
        tulaj=reszek[3]
        indianok.append(Indian(nev, nem, kor, tulaj))
    
    #4.3
    print(f"{len(indianok)} indián van a listán.")

    #4.4
    seged=[]
    for item in indianok:
        if item.tulaj not in seged:
            seged.append(item.tulaj)
    print(f"{len(seged)} féle eszköz szerepel a leltárban.")

    #4.5
    ferfi=0
    no=0
    for item in indianok:
        if item.nem=="n":
            no+=1
        else:
            ferfi+=1
    print(f"{no} nő és {ferfi} férfi van a törzsben.")

    #4.6
    tom=0
    for item in indianok:
        if item.tulaj=="tomahawk":
            tom+=1
    print(f"{tom} tomahawkja van a törzsnek.")

    #4.7
    venek=[]
    for item in indianok:
        if item.tulaj=="békepipa":
            venek.append(item)
    print("A vének tanácsa:")
    for item in venek:
        print(f"{item.nev}, {item.nem}, {item.kor}")
    
    #4.8
    mezitlab=0
    for item in indianok:
        if item.tulaj!="mokaszin":
            mezitlab+=1
    print(f"{mezitlab} mezitlábas van a törzsben.")

    #4.9
    ossz=0
    for item in indianok:
        ossz+=item.kor
    atlag=ossz/len(indianok)
    print(f"Az átlag életkor {atlag} év a törzsben.")

def main():
    fel4()

    

main()