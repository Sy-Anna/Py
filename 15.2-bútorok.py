
butorok=[]
with open('butorok.txt', mode='r', encoding='utf-8') as fajl:
    for sor in fajl:
        butorok.append(sor.strip().replace("\"","").split(" "))

print(butorok)



def massalh():
    #maganhangzok=["e" "u" "i" "i" "o" "ő" "ú" "ö" "ü" "ó" "a" "é" "á" "ű" "í"]
    massalhangzok=["q" "w" "r" "t" "z" "p" "s" "d" "f" "g" "h" "j" "k" "l" "y" "x" "c" "v" "b" "n" "m"]

    """for szo in butorok:
        for i in range (len(szo)):
            if (szo[i]) in maganhangzok:
                """
    massalh_szavak=[]
    for szo in butorok:
        if szo[0] in massalhangzok:
            massalh_szavak.append(szo)
            print(szo)
    print(massalh_szavak)

def hosszu():
    hosszu=[]
    for szo in butorok:
        if len(szo)>=5:
            print(szo)
            hosszu.append(szo)
    print(hosszu)

massalh()
hosszu()