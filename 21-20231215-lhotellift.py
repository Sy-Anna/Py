class Lift:
    datum=0
    sorszam=0
    start=0
    cel=0

    def __init__(self, datum, sorszam, start, cel) -> None:
        self.datum=datum
        self.sorszam=sorszam
        self.start=start
        self.cel=cel

    def __str__(self) -> str:
        return f"{self.datum} {self.sorszam} {self.start} {self.cel}"

hotelLift=[]
def beolvasas():
    f=open('lift.txt', encoding='UTF-8')
    for sor in f:
        reszek=sor.strip().split(" ")
        datum=reszek[0]
        sorszam=int(reszek[1])
        start=int(reszek[2])
        cel=int(reszek[3])
        hotelLift.append(Lift(datum, sorszam, start, cel))

def fel3():
    print(f"3. feladat: Összes lifthasználat: {len(hotelLift)}")

def fel4():
    utolso=len(hotelLift)-1
    print(f"4. feladat: Időszak: {hotelLift[0].datum} - {hotelLift[utolso].datum}")

def fel5():
    max=hotelLift[0]
    for item in hotelLift:
        if item.cel>max.cel:
            max=item
    print(f"5. feladat: Célszint max: {max.cel}")

def fel6():
    kartya=int(input("Kártya száma: "))
    celszint=int(input("Célszint száma: "))
    return kartya, celszint

def fel7():
    valasz=fel6()
    kartya=valasz[0]
    celszint=valasz[1]
    found=0
    szam=0
    while szam<=len(hotelLift)-1 and found==0:
        for item in hotelLift:
            if item.sorszam==kartya and item.cel==celszint:
                found+=1
                break
        szam+=1
    if found==0:
        print(f"A(z) {kartya} kártyával nem utaztak a(z) {celszint}. emeletre!")
    else:
        print(f"A(z) {kartya} kártyával utaztak a(z) {celszint}. emeletre!")
    
def fel8():
    print("8. feladat: Statisztika")
    datumok=[]
    for item in hotelLift:
        if item.datum not in datumok:
            datumok.append(item.datum)
    szam=0
    while szam<=len(datumok)-1:
        found=0
        for item in hotelLift:
            if item.datum==datumok[szam]:
                found+=1
        print(f"\t{datumok[szam]} - {found}")
        szam+=1


def main():
    beolvasas()
    fel3()
    fel4()
    fel5()
    fel7()
    fel8()

main()