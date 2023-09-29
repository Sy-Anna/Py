#szam1 = int(input("kérek egy számot: "))
#szam2 = int(input("kérek egy másik számot: "))
#
#if szam1 > szam2:
#    print(f"{szam1} > {szam2}")
#else:
#    print(f"{szam1} nem nagyobb, mint {szam2}")
#
#    if aOldal+bOldal > cOldal and bOldal+cOldal>aOldal and aOldal+cOldal>bOldal:
#    print("A háromszög szerkeszthető!")
#    K= aOldal+bOldal + cOldal
#    print(f"A háromszög kerülete: {K}")
#else:
#    print("A háromszög nem szerkeszthető!")

#if logikai feltétel legyen, ami vagy true vagy false 
#if aOldal == 6:

#17


#szam= int(input("szam:  "))
#if szam > 0:
#    print(f"+{szam}")
#if szam<0:
#    print(f"{szam}")
#else:
#    print(f"nulla")



#pontszam= int(input("Pontszám: "))
#if pontszam <= 42:
#    print("elégtelen")
#elif pontszam <= 57:
#    print("Elégséges")
#elif pontszam<72:
#    print("közepes")
#elif pontszam<87:
#    print("Jó")
#else:
#    print("jeles")


#print(f"A megadott pont:  {pontszam}")
#
#szam= int(input("Kérem a számot: "))
#
#if szam % 10 == 0:
#    print("A szám osztható tízzel!")
#    print("Süt a nap")
#    print("Az élet szép")
#else:
#    print(f"A szám bnem osztható 10-zel, a maradék: {szam%10}")    
#    print("Ez itt az else ág")



#szamlalo= int(input("Szamlalo: "))
#nevezo= int(input("nevezo: "))
#if nevezo != 0:
#    print(f"Eredmény: {szamlalo/nevezo}")
#else:
#    print("Nullával nem osztunk")



egyikSzam= int(input("Kérem az első számot: "))
masikSzam= int(input("Kérem a második számot: "))
#= értékadás. A logikai változó kap értéket
# két kifejezést kötünk össze egy and -de: ha mindkét feltétel igaz, 
# akkor a logikai változó értéke is igaz lesz: True, 
# ellenkező esetben False
logikai = egyikSzam>0 and masikSzam>0

print(f"Mindkét szám pozitív: {logikai}")
#ha legalább az egyik feltétel teljesül, akkor igaz lesz
logikai = egyikSzam>0 or masikSzam>0
print(f"Legalább az egyik szám pozitiv {logikai}")

#Táblázatos igazságtábla, melyben az 1: true, a 0 false értéket takar
# A | B |  A and B 
# 1 | 1 |     1
# 1 | 0 |     0
# 0 | 1 |     0
# 0 | 0 |     0

A= True
B= True
print(f"{'  A'} | {'  B '}|  A and B ")
print(f"{A:3} | {B:3} |  {A and B} ")
A= False
print(f"{A:3} | {B:3} |  {A and B} ")
A= True
B= False
print(f"{A:3} | {B:3} |  {A and B} ")
A=False
print(f"{A:3} | {B:3} |  {A and B} ")