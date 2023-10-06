import random
harcosHP = 100
szornyHP = 100
while harcosHP>0 and szornyHP>0:
    sebzes = 0
    #harcos köre:
    while True:
        print("Dobj egyet a kockával (enter): ")
        input()
        kocka = random.randint(1, 6)
        print(f"A dobásod: {kocka}")
        print()
        sebzes += kocka
        if kocka == 1:
            print("Elestél, ebben a körben nem sebezted meg a szörnyet!")
            print()
            sebzes = 0
            break
        valasz = input("szeretnél újat dobni? (i/n)")
        print()
        if valasz == "n":
            break
    szornyHP-=sebzes
    print(f"A szörny hp-ja: {szornyHP}")
    print()
    #szörny köre:
    sebzes = 0
    for i in range (3):
        kocka = random.randint( 1, 6)
        print(f"A szörny dobása: {kocka}")
        sebzes+=kocka
    print()
    harcosHP -= sebzes
    print(f"A hp-d {harcosHP}")
    print()
if harcosHP>szornyHP:
    print("A harcos véres küzdelemben legyőzte a szörnyet, és elnyerte a hercegnő kezét.")
else:
    print("A szörny véres küzdelemben legyőzte a harcost és elnyelte a hercegnő kezét")