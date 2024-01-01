import random
def egyeniPontszam():
    return random.randint(0,5)

def csapatPontszam():
    lista= []
    for i in range(7):
        lista.append(egyeniPontszam() *10)
    return lista    

def pontOsszesites(lista):
    return sum(lista)

def gyoztes(sorszam, urmacskak, szuperegerek):
    urmacskakPontja= pontOsszesites(urmacskak)
    print(f"{sorszam}. kör:")
    print(f"\tŰrmacskák: ", end = "")
    print(*urmacskak,sep=" ", end = " ->")
    print(urmacskakPontja)

    szuperegerekPontja= pontOsszesites(szuperegerek)
    print(f"\tSzuperegerek: ", end = "")
    print(*szuperegerek,sep=" ", end = " ->")
    print(szuperegerekPontja)   
    return urmacskakPontja > szuperegerekPontja


def jatek():
    gyoztesMeccsekSzama = 0
    for i in range(1,8):
        urmacskak = csapatPontszam()
        szuperegerek = csapatPontszam()
        gyozE = gyoztes(i, urmacskak, szuperegerek)
        if gyozE:
            gyoztesMeccsekSzama+=1
    print("Ádám győzelmeinek száma:", gyoztesMeccsekSzama)


def main():
    jatek()

main()    

