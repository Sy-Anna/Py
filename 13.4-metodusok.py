import random
"""
irjunk metódust, ami megkap egy főnevet, és visszatér a hozzá illő névelővel
irjunk metódust, ami bekér egy főnevet, és kiir egy véletlen mondatot vele. Pl:
sapka
A sapka kék. 
irjunk metódust, ami vékletlenszerűen kiválaszt egy színt (jelzőt), és visszatér vele.
"""


def randomMondat():
    #lokális változó: csakl ebben a metódusban él, csak ebben látszódik
    fonev= input("Kérek egy főnevet:")
    print(f"{nevelo(fonev)} {fonev} {ramdomSzin()} ")

def nevelo(fn):
    mgh= "aáeéiíoóöőuúüű"
    if fn[0].lower() in mgh:
        return "Az"
    else:
        return "A"

def ramdomSzin():
    szinek= ["piros", "zöld", "fehér", "sárga", "kék"]
    return random.choice(szinek)

def main():
    randomMondat()


main()    

















