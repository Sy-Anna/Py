import math
import locale
import functools


def konyvtar():
    konyvek=["Madách Imre: Az ember tragédiája", "Molnár Ferenc: A Pál utcai fiúk", "Gárdonyi Géza: Egri csillagok", "Kosztolányi Dezső: Édes Anna"]
    kikolcsonzott=[]
    while True:
        print("Könyvek:", konyvek, "\n")
        print("Kikölcsönzött könyvek: ", kikolcsonzott, "\n")
        valasz=int(input("Könyv kereséshez nyomja meg az 1-es gombot!\nÚj könyv felvételéhez nyomja meg a 2-es gombot!\nKölcsönzéshez nyomja meg a 3-mas gombot!\nKönyv visszavételéhez nyomja meg a 4-es gombot!\nA ciklusból való kilépéshez nyomja meg a 0 gombot!\n"))
        if valasz==1:
            kereses=input("Melyik könyvet keresi? (Szerző: Cím) " )
            if kereses in konyvek:
                print(f"A keresett könyv indexe {konyvek.index(kereses)}\n")
            else:
                print("A keresett könyv nem található a könyvtárban!\n")
        elif valasz==2:
            uj_konyv=input("Adja meg az új könyv szerzőjét és címét: (Szerző: Cím) ")
            if uj_konyv in konyvek:
                print("A könyv már szerepel az adatbázisban!\n")
            else:
                konyvek.append(uj_konyv)
                print("A könyvfelvétel sikeresen megtörtént!\n")
        elif valasz==3:
            kolcsonzes=input("Ajda meg a kölcsönözni kívánt könyv szerzőjét és címét: (Szerző: Cím) ")
            if kolcsonzes in kikolcsonzott:
                print("A könyv már  ki van kölcsönözve!\n")
            elif kolcsonzes in konyvek:
                konyvek.remove(kolcsonzes)
                kikolcsonzott.append(kolcsonzes)
                print("Sikeres kölcsönzés!\n")
            else:
                print("A köyónyv nem található meg a könyvtárunkban!\n")
        elif valasz==4:
            vissza=input("Adja meg a visszavinni kívánt könyv szerzőjét és címét: (Szerző: Cím) ")
            if vissza in konyvek:
                print("Ez a könyv már vissza lett hozva!\n")
            elif vissza in kikolcsonzott:
                konyvek.append(vissza)
                kikolcsonzott.remove(vissza)
                print("A könyv sikeresen visszahozva!\n")
            else:
                print("A köyónyv nem található meg a könyvtárunkban!\n")
        elif valasz==0:
            print("Köszönjük a látogatását könyvtárunkba!\n")
            break
        else:
            print("Ilyen menüpont nincs!\n")

def szallas():              #ashdjfhaskjflsaf
    vendegek=0
    ures_szoba=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    foglalt_szoba=[]
    felig_ures=0
    teli=0
    ures=12
    while True:
        foglalas=[]
        valasz=int(input("Szoba foglalásához nyomja meg az 1-es gombot!\nFoglalás törléséhez nyomja mega 2-es gombot!\n"))
        if valasz==1:
            foglalas.clear
            fo=int(input("Hány főre szeretne foglalni? "))
            if vendegek+fo<=24:
                vendegek+=fo
                if fo==1:
                    foglalas.append(ures_szoba.index(0))
                    foglalt_szoba.append(ures_szoba.index(0))
                    ures_szoba.remove(ures_szoba.index(0))
                    felig_ures+=1
                    ures-=1
                if fo%2==0:
                    for i in range (fo/2):
                        foglalas.append(ures_szoba.index(i-1))
                        foglalt_szoba.append(ures_szoba.index(i-1))
                        ures_szoba.remove(ures_szoba.index(i-1))
                    teli+=fo/2
                    ures-=fo/2
                    print ("Az önök álltal elfoglalt szobák:", foglalas)
                if fo%2>0:
                    for i in range (math.ceil(fo/2)):
                        foglalas.append(ures_szoba.index(i-1))
                        foglalt_szoba.append(ures_szoba.index(i-1))
                        ures_szoba.remove(ures_szoba.index(i-1))
                    teli+=(fo//2)
                    felig_ures+=1
                    ures-=math.ceil(fo/2)
                    print ("Az önök álltal elfoglalt szobák:", foglalas)
                else:
                    print("Sajnáljuk, nincs ennyi szabad helyünk!")
            
                

def sutemeny(): #majdnem
    sutik= ['csokis brownie', 'almás pite', 'mogyorós keksz', 'mézeskalács', 'kókuszos szelet', 'tejszínes pite', 'citromos muffin', 'vaníliás fánk', 'eperkrém torta', 'almás-fahéjas palacsinta', 'karamellás popcorn', 'mandulás torta', 'datolyás sütemény', 'túrófánk', 'meggyes pite', 'almás süti', 'puncsos torta', 'citromhabos sütemény', 'diós tekercs', 'narancsos piskóta']
    print(sutik)
    mennyi=len(sutik)
    csokis=0
    print(f"A kínálatunkban {mennyi} süti van!")
    print(sutik.count("csokis"))
    leghoszabb=max(sutik, key=len)
    print("A leghosszabb nevű sütemény a(z)", leghoszabb)
    locale.setlocale(locale.LC_ALL, "HU_hu.UTF8")
    beturend=sutik.sort(key=functools.cmp_to_key(locale.strcoll))
    print(beturend)
    print(sutik.count("muffin"))
    if 'mogyorókrémes linzer' in sutik:
        print("A sütik között van mogyorókrémes linzer is!")
    else:
        print("Sajnos nincs a sütik között mogyorókrémes linzer!")
    acm=[]
    for i in range (mennyi):
        if sutik[i-1][0]=='a' or sutik[i-1][0]=='c' or sutik[i-1][0]=='m':
            acm.append(sutik[i-1])
    print("az a, c, és m betükkel kezdődő sütik:", acm)
    kaloria=mennyi*2*120
    print(kaloria, "kalóriát viszünk be, ha az összes sütiből eszünk kettőt.")
    szam=0
    paros=[]
    for i in range (mennyi):
        if szam%2==0 and szam>0:
            paros.append(sutik.index(szam))
    print("a páros indexű sütik:", paros)
    vissza = [i[::-1] for i in sutik]
    print("A sütik visszafelé:", vissza)


def huto():
    huto=["dinnye", "sárgadinnye", "sütőtök", "dió", "sajt", "szalámi", "tej", "felvágott"]
    kint=[]
    while True:
        print("Hűtő: ", huto, "\n")
        print("kint:", kint, "\n")
        valasz=int(input("1-es gomb: ételek listázása\n2-es gomb: étel kivétele a hűtőből\nÉtel berakása a hűtőbe\n4-es gomb: Takarítás\n5-ös gomb: kilépés\n"))
        if valasz==1:
            print(huto)
        elif valasz==2:
            etel=int(input("Melyik ételt szeretnéd kivenni a hűtőből? "))
            if etel in huto:
                huto.remove(etel)
                kint.append(etel)
                print("Jó étvágyat!\n")
            else:
                print("Ezt már a múlthéten megetted!\n")
        elif valasz==3:
            etel=int(input("Mit szeretnél betenni a hűtőbe? "))
            if etel in huto:
                print("Ezt már beraktad!\n")
            else:
                huto.append(etel)
                if etel in kint:
                    kint.remove(etel)
                print("Bent is van!\n")
        elif valasz==4:
            szam=0
            for i in range (len(huto)):
                kint.append(huto[szam])
                huto.remove(huto[szam])
                szam+=1
            print("Mindent kivettél a hűtőből!\n")
        elif valasz==5:
            print("Kilépés\n")
            break

