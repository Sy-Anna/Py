# for ciklus: előre meghatározza hányszor fusson le. pl 10-szer, 456-szor
# for i in range (kezdőérték, végárték+1, lépésköz)
# i: ciklusváltozó
# in: valamin megy végig
# range: sorba veszi az értékeket
# i: felveszi a kezdőértéket, majd annyival növekszik, amennyi a lépésköz mértéke
# mikor áll le a ciklus: ha az i eléri a végértéket: az már nem fut


for i in range (0, 10, 1):
    print (i, end= " ")
print (" ")
print (" ")
for i in range (10):
    print(i, end= " ")
print (" ")
print (" ")
for i in range (2, 21, 2):
    print(i, end= (" "))
print (" ")
print (" ")
for i in range (1,11):
    print(f"{i} Egy fecske nem csinál nyarat")
print (" ")
print (" ")
#n = int(input("Hányszor írjuk ki: "))
#for i in range (1, n+1):
#    print(f"{i}. Megmondtam már százszor, {n}-szer nem írom ki!")
print (" ")
print (" ")
for i in range (1,100):
    if i%7==0:
        print(i,end=" ")
print (" ")
print (" ")
for i in range (0,100,7):
    print (i, end=" ")

# = értéket adok meg
# == relációt vizsgálok

ossz = 0
for i in range (42+1):
    ossz = ossz+i
print(ossz)

print(" ")
print(" ")

db = 0
for i in range (1000, -1, -1):
    if i%2==0 and i%3==0:
        db += 1
print(f"db: {db}")

print(" ")
print(" ")

#kezdo = 1
#eredmeny = 1
#szam = int(input("Szám: "))
#for i in range (1, szam):
#    kezdo= kezdo+1
#    eredmeny= kezdo*eredmeny
#print(f"Az eredmény {eredmeny}")
print(" ")
print(" ")
for i in range (1,11):
    print(f"{i}*7= {i*7}")
print(" ")
print(" ")
for i in range (1,11):
    for j in range(1,8): #amig a belső for le nem fut, a külső nem lép tovább
        print(f"{i:2}*{j:2} = {i*j:2}", end= "   ")
    print ()