class Met:
    telepules=""
    ido=0
    szelirany=""
    homerseklet=0

    def __init__(self, telepules, ido, szelirany, homerseklet):
        self.telepules=telepules
        self.ido=ido
        self.szelirany=szelirany
        self.homerseklet=homerseklet

    def __str__(self) -> str:
        return f"{self.telepules} {self.szelirany} {self.ido} {self.homerseklet}"

def ora(ido):
    ora=ido//100
    perc=ido%100
    teljes=f"{ora:3}:{perc:3}"
    return teljes

jelentes=[]
def beolvasas():
    f=open("tavirathu13.txt", encoding="UTF-8")
    for sor in f:
        szavak=sor.strip().split(" ")
        telepules=szavak[0]
        ido=int(szavak[1])
        szelirany=szavak[2]
        homerseklet=int(szavak[3])
        jelentes.append(Met(telepules, ido, szelirany, homerseklet))

def fel2():
    kod=str(input("2. feladat\nAdja meg egy település kódját! Település: "))
    seged=[]
    for item in jelentes:
        if item.telepules==kod:
            seged.append(item.ido)
    print(f"Az utolsó mérési adat a megadott településről {ora(max(seged))}-kor érkezett.")
        
def fel3():
    legalacsonyabb=jelentes[0]
    legmagasabb=jelentes[0]
    for item in jelentes:
        if item.homerseklet>legmagasabb.homerseklet:
            legmagasabb=item
        elif item.homerseklet<legalacsonyabb.homerseklet:
            legalacsonyabb=item
    print(f"3. feladat\nA legalacsonyabb hőmérséklet: {legalacsonyabb.telepules} {ora(legalacsonyabb.ido)} {legalacsonyabb.homerseklet} fok.\nA legmagasabb hőmérséklet: {legmagasabb.telepules} {ora(legmagasabb.ido)} {legmagasabb.homerseklet} fok.")
    

def fel4():
    found=0
    print("4. feladat")
    for item in jelentes:
        if item.szelirany=="00000":
            found+=1
            print(item.telepules, ora(item.ido))
    if found==0:
        print("Nem volt szélcsend a mérések idején.")

def fel5():
    print("5. feladat")
    varosok=[]
    for item in jelentes:
        if item.telepules not in varosok:
            varosok.append(item.telepules)
    szam=0
    while szam<=8:
        seged=[]
        atlag=0
        for item in jelentes:
            if item.telepules==varosok[szam]:
                seged.append(item)
        max=seged[0].homerseklet
        min=seged[0].homerseklet
        for item in seged:
            atlag+=item.homerseklet
            if item.homerseklet<min:
                min=item.homerseklet
            elif item.homerseklet>max:
                max=item.homerseklet
        ing=max-min
        atlag=atlag/len(seged)
        print(f"{varosok[szam]} középhőmérséklet: {round(atlag)}; hőmérséklet ingadozás: {ing}")
        szam+=1

def fel6():
    print("6. feladat")
    varosok=[]
    for item in jelentes:
        if item.telepules not in varosok:
            varosok.append(item.telepules)
    f=open('x.txt', "x")

            

def main():
    beolvasas()
    #fel2()
    fel3()
    fel4()
    fel5()

main()