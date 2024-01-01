gyumolcsok=[]

with open('gyumolcsok.csv', mode='r', encoding='utf-8') as fajl:
    for szo in fajl:
        gyumolcsok.append(szo.strip().replace("\"","").split(";"))


def szavak():
    for szo in gyumolcsok:
        if len(szo)>2:
            print(szo)

        
szavak()
print(f"{len(gyumolcsok)} gyümölcs van a listán.")
