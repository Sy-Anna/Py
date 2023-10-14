import random

nyerA=0
nyerP=0
n=int(input("Hány kört játszon Anni és Panni? "))
for i in range (n):
    dob1=random.randint(1,6)
    dob2=random.randint(1,6)
    dob3=random.randint(1,6)
    osszeg=dob1+dob2+dob3
    if osszeg>=10:
        nyertes="Panni"
        nyerP+=1
    if osszeg<10:
        nyertes="Anni"
        nyerA+=1
    print(f"Dobás: {dob1} + {dob2} + {dob3} = {osszeg}, nyert {nyertes}")
print(f"A játék során Anni {nyerA} alkalommal, Panni pedig {nyerP} alkalommal nyert.")