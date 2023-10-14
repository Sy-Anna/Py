import random

nyerA=0
nyerP=0
n=int(input("Hány kört játszon Anni és Panni? "))
for i in range (n):
    Anni = 0
    Panni = 0
    print(f"{i+1}. kör")
    for j in range (3):
        dobA=random.randint(1,6)
        dobP=random.randint(1,6)
        print(f"Anni dobása: {dobA}")
        print(f"Panni dobása: {dobP}")
        Anni+=dobA
        Panni+=dobP
    print(f"Anni pontszáma: {Anni}")
    print(f"Panni pontszáma: {Panni}")
    if Anni<10:
        nyerA+=1
    if Panni>10:
        nyerP+=1
print(f"Anni {nyerA} alkalommal, Panni pedig {nyerP} alkalommal nyert.")