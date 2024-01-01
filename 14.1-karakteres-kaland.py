import random

def kezdeti_allapot():
    herkElet=random.randint(10,15)*10
    vikiElet=random.randint(10,15)*10
    print(f"Herkules élete={herkElet}\nViktória élete={vikiElet}")
    return herkElet, vikiElet

def kihivas (kor):
    szint=kor
    hKepesseg=["ütés", "rúgás"]
    vKepesseg=["kardhasítás", "eltűnés"]
    hHasznal=random.choice(hKepesseg)
    vHasznal=random.choice(vKepesseg)
    hSebzese=sebzodes(szint, hHasznal)
    vSebzese=sebzodes(szint, vHasznal)
    print(f"Herkules a(z) {hHasznal} képességét használta, ezzel {hSebzese} életet vett el Viktóriától.")
    print(f"Viktória a(z) {vHasznal} képességet használta, ezzel {vSebzese} életet vett el Herkulestől.")
    return vSebzese, hSebzese


def sebzodes (kor, kepesseg):
    valasz=kepesseg
    szint=kor
    if valasz=="ütés":
        sebzes=szint*10
    elif valasz=="rúgás":
        sebzes=szint*15
    elif valasz=="kardhasítás":
        sebzes=szint*12
    elif valasz=="eltűnés":
        sebzes=szint*8
    else:
        sebzes=100
    return sebzes

def jatek():
    eletek=kezdeti_allapot()
    herkElete=eletek[0]
    vikiElete=eletek[1]
    kor=1
    while kor<=5:
        input("~~Nyomj entert a folytatáshoz!~~")
        print(f"{kor}. kör")
        sebzesek=kihivas(kor)
        herkElete-=sebzesek[0]
        vikiElete-=sebzesek[1]
        print(f"Herkules élete: {herkElete}\nViktória élete: {vikiElete}")
        if kor<5:
            if herkElete<=0 or vikiElete<=0:
                if herkElete<=0 and vikiElete<=0:
                    print("Mindkét játékos élete elfogyott\n")
                elif herkElete>vikiElete:
                    print("Elfogyott Viki élete\n")
                else:
                    print("Elfogyott Herkules élete\n")
                break
        kor+=1
    gyoztes=gyoz(herkElete, vikiElete)
    if gyoztes==0:
        print("A verseny döntetlen")
    elif gyoztes==1:
        print("Herkules győzött")
    elif gyoztes==2:
        print("Viki győzött")

def gyoz(elet1, elet2):
    if elet2==elet1:
        gyoztes=0
    elif elet1>elet2:
        gyoztes=1
    else:
        gyoztes=2
    return gyoztes        

def main():
    jatek()

main()