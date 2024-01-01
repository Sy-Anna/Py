import random

def dobas():
    return random.randint(1,6)


def pontszamitas(nev, dobasokSzama):
    ossz=0
    print(f"{nev} dobasai: ", end= "")
    for i in range(dobasokSzama):
        kocka= dobas()
        ossz+= kocka
        print(kocka,end = " ")
    print(f"Összpontszám: {ossz}")
    return ossz


def gyoztes(nev1, nev2):
    kocka= dobas()
    pont1= pontszamitas(nev1, kocka)
    pont2= pontszamitas(nev2, kocka)
    if pont1>pont2:
        return nev1
    elif pont1 == pont2:
        return "Döntetlen"
    else:
        return nev2
    
def jatek():
    nev1= "Ádám"
    nev2= "Tamás"
    for i in range(1,6):
        print(f"{i}. kör: ")
        nyertes= gyoztes(nev1, nev2)
        print(f"A győztes: {nyertes}")

def main():
    jatek()



main()

