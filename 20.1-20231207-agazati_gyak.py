import random

def nagyobb():    
    szam1=int(input("Adjon meg egy számot! "))
    szam2=int(input("Adjon meg egy másik számot! "))
    if szam1==szam2:
        print("A két szám egyenlő")
    else:
        print(f"A nagyobb érték {max(szam1, szam2)}")

def szavak():
    szo1=str(input("Adj meg egy szót! "))
    szo2=str(input("Adj meg egy másik szót! "))
    if len(szo1)==len(szo2):
        print("A két szó egyforma hosszú.")
    elif len(szo1)>len(szo2):
        print(f"A hosszabb szó: {szo1}")
    elif len(szo2)>len(szo1):
        print(f"A hosszabb szó: {szo2}")
    
def nyitvatartas():
    most=int(input("Hány óra an most? "))
    if most>=8 and most<16:
        print(f"A bolt nyitva van.\nEnnyi órád van még odaérni: {16-most}")
    else:
        print("A bolt zárva van.")

def raketa():
    terv=int(input("Hány órás visszaszámlálást tervezünk? "))
    felfuggesztes=0
    vissza=terv
    while vissza>0:
        print(f"Visszaszámlálás: {vissza}")
        valasz=str(input("Fel kell függeszteni a visszaszámlálást? (i/n) "))
        if valasz=="i":
            felfuggesztes+=1
        vissza-=1
    print(f"A rakéta a visszaszámlálást követően ennyi órával indult: {terv+felfuggesztes}")

def jelszo():
    nev="bori99"
    jelszo="Szivecske<3"
    felhaszn=str(input("Adja meg a felhasználónevét! "))
    jelsz=str(input("Adja meg a jelszavát! "))
    if felhaszn!=nev or jelsz!=jelszo:
        print("Belépés megtagadva!")
    else:
        print("Belépés engedélyezve!")

def vizsga():
    def sikeres(pont):
        if pont<48:
            sikeres=False
        else:
            sikeres=True
        return sikeres

    while True:
        nev=str(input("Adja meg a vizsgázó nevét! "))
        if nev=="":
            break
        pontszam=int(input("Adja meg a pontszámát! "))
        if sikeres(pontszam)==True:
            input(f"{nev} vizsgája sikeres.")
        else:
            input(f"{nev} vizsgája sikertelen.")

def kedvencfilm():
    cim=str(input("Adja meg a film címét!"))
    hossz=int(input("Hány perces a film? "))
    print(f"A(z) {cim} című film {hossz//60} óra {hossz%60} perc hosszú.")

def nevelo(szo):
    last=len(szo)
    betu=""
    szam=0
    for item in szo:
        szam+=1
        if szam==last:
            betu=item
    maganhangzok=["a","á","e","é","i","í","o","ó","ö","ő","u","ú","ü","ű"]
    if betu in maganhangzok:
        return "Az"
    else:
        return "A"

def jelzo():
    jelzok=["nagy", "piros", "szép", "kerek"]
    return random.choice(jelzok)

def mondatok():
    fonev=str(input("Adjon meg egy főnevet! "))
    print(f"{nevelo(fonev)} {fonev} {jelzo()}.")


def main():
    pass

main()