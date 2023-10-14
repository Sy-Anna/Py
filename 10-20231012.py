import math
import random

#def kulcsszó nev()
# minden egy tabbal bentebb van, ami a metódusba kerül

def feladat1():
    while True:
        n=int(input("nem negatív szám: "))
        if n>=0:
            break



def feladat2():
    osszeg=0
    menny=0
    while True:
        n=int(input("kérek egy számot: "))
        if n==0:
            print(f"{osszeg}Ft")
            print(f"{menny}db")
            break
        else:
            osszeg+=n
            menny+=1
        

#ebben hívunk meg mindent amit futtatni szeretnénk
def main():
    print("Mainben vagyok")
    feladat2()


def feladat3():
    ertek=["fej", "írás"]
    while True:
        erme=random.choice(ertek)
        valasz=input("Fej vagy írás?")
        if valasz == erme:
            print("Helyes!")
        elif valasz=="0":
            break
        else:
            print("Nem jó!")

def feladat4():
    print("Szám kitalálós játék")
    print("Nehézségi szint: könnyű, nehéz, vagy hardcore?")
    valasz = input("A válaszom: ")
    if valasz == "könnyű":
        szam = random.randint(1, 10)    
    if valasz == "nehéz":
        szam = random.randint(1, 100)
    if valasz == "hardcore":
        szam = random.randint(1, 1000)
    elet = 7
    while True:
        print(f"Életek száma: {elet}")
        tipp = int(input("tipp= "))
        if tipp == szam:
            print("Gratulálok!")
            break
        else:
            elet-=1
            print("Nem jó!")
        if elet == 0:
            print("Elfogytak az életeid!")
            print(f"A szám {szam} volt.")
            break

def feladat5():
    operator = ["+", "-", "*"]
    kerdes=10
    pont=0
    while kerdes>0:
        muvelet=random.choice(operator)
        szam1=random.randint(1,10)
        szam2=random.randint(1,10)
        while True:
            if muvelet=="+":
                eredmeny=szam1+szam2
            elif muvelet=="-":
                eredmeny=szam1-szam2
            elif muvelet=="*":
                eredmeny=szam1*szam2
            valasz=int(input(f"{szam1}{muvelet}{szam2}= "))
            if valasz==eredmeny:
                print("Helyes!")
                kerdes-=1
                pont+=1
                break
            else:
                print("Nem jó!")
                kerdes-=1
                break
    print(f"{pont*10}%-ot értél el!")

def feladat6():
    kezdo=0
    ugras=100
    elore=1
    csiklandos=0
    while ugras>0:
        kezdo+=elore
        kezdo-=1
        elore+=1
        ugras-=2
        if kezdo%5==0:
            csiklandos+=1
    print(f"100 ugrás után a bolha {kezdo} értéknél lesz.")
    print(f"A bolha {csiklandos-1} csiklandós pontot érintett.")

def feladat7():
    x=0
    y=0
    irany=1
    lepes=0
    while lepes<50:
        if irany%2==0:
            y+=1
        else:
            x+=1
        if (x**2+y**2)%3==0 or (x**2+y**2)%5==0:
            irany+=1
        lepes+=1
        print(f"x{x}, y{y}")
    print(f"A hangya koordinátái 50 lépés múlva: x:{x}, y:{y}")

def feladat8():
    elet=100
    szint=0
    veszely=["Találkozik egy nagy, éhes tigrissel.", "Átkel egy veszélyes folyón, és az áramlat elragadja.", "Megbotlik egy csapdában.", "Eltéved a dzsungelben.", "Egy mérgező kígyó támad rá."]
    valasz=input("Melyik úton keljen át a kalandor? A hídon, vagy az úton? (híd/út)")
    if valasz=="híd":
        print("A kalandor biztonságban van, és elérte az utazás célját.")
    if valasz=="út":
        while elet>0:
            print(random.choice(veszely))
            dobas=random.randint(1,6)
            if dobas<61:
                elet-=dobas
            if dobas==6:
                szint+=1
                print("Léptél egy szintet!")
            if szint==5:
                print("Nyertél, átjutottál!")
                break
            else:
                print(f"{dobas}-t dobtál!")
                print(f"{elet} életed maradt.")
                input("Lépj mégegyet!")
                if input==0:
                    break
    if elet==0:
        print("Meghaltál :()")

feladat8()