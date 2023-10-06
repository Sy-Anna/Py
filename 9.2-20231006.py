import random
panni = 0
panni_ossz=0
anni = 0
anni_ossz=0
korok_szama = int(input("Hány kör legyen? "))
for i in range (korok_szama):
    for j in range (3):
        kocka = random.randint(1,6)
        print(f"Anni dobása: {kocka}")
        anni += kocka
        kocka = random.randint(1,6)
        print(f"Panni dobása: {kocka}")
        panni += kocka
    print(f"Anni pontszáma: {anni}")
    print(f"Panni pontszáma: {panni}")
    if anni <10:
        print("Anni nyert!")
        anni_ossz+=1
    if panni >10:
        print("Panni nyert!")
        panni_ossz+=1
