import random

szam1 = random.randint (1,100)
szam2 = random.randint (1,100)
szam3 = random.randint (1,100)
print(szam1, szam2, szam3)
print(f"A három szám összege: ", szam1+szam2+szam3)

szam4 = random.randint (-100,0)
print(szam4)

ora1 = random.randint (0,24)
perc1 = random.randint (0,60)
mp1 = random.randint (0,60)
ora2 = random.randint (0,24)
perc2 = random.randint (0,60)
mp2 = random.randint (0,60)
elso = ora1*60*60+perc1*61+mp1
masodik = ora2*60*60+perc2*60+mp2
print(f" {ora1}:{perc1}:{mp1}; {ora2}:{perc2}:{mp2}")
print(f"A két időpont közti különbség {abs(elso-masodik)} mp.")
