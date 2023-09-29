#interakciók, ciklusok:

#-ismétlődő utasítások, ciklusok / ciklus mag / ciklus törzse
#-ismétlésre vonatkozó feltétel
#-ciklus változó
#-léptetés

#határpzott lépsszámú

#for i in range(6):
#    print ("hello word")
#    print (i)
#
#print (" ")
#
#for i in range(2,6):
#    print (i)
#
#print (" ")
#
#for i in range (2,16,3):
#    print(i)
#
#print (" ")
#print ("1. feladat")
#print (" ")
#
#for i in range (1, 51):
#    print (i)
#
#for i in range (182,213):
#    print (i)

#for i in range (100,201, 2):
#    print (i)
#
#for i in range (89,56, 2):
#    print (i)
#
#for i in range (1, 21):
#    print (i, i*i)
#
#for i in range (99, 0, -3):
#    print (i)
#
#for i in range (100, 50-1, -5):
#    print (i*2)

#for i in range (1, 1001):
#    if i <1000:
#        print (f"{i},")
#    else:
#        print (f"{i}.")

print (" ")
print ("2. feladat")
print (" ")

#for i in range (100):
#    print ("*")

#bekert = int(input("kérek egy számot:"))
#darab = int(input("Hányszor írjam ki?"))
#for i in range (darab):
#    print(bekert)

#bekert = input("Adjon meg valamit: ")
#keret = ""
#for i in range (len(bekert)+4):
#    keret += "*"
#print(keret)
#print(f"* {bekert} *")
#print(keret)

#|__|XX|__|
#|XX|__|XX|

fekete = "|_|"
feher = "X"
elso = f"{fekete}{feher}{fekete}{feher}{fekete}{feher}{fekete}{feher}|"
masodik = f"|{feher}{fekete}{feher}{fekete}{feher}{fekete}{feher}{fekete}"
for i in range(8):
    if i%2==0:
        print(elso)
    else:
        print(masodik)


elso = int(input("Első szm: "))
masodik = int(input("Második szám: "))
lepeskoz = int(input("Lépésköz: "))
if elso > masodik:
    nagyobb = elso+1
    kisebb = masodik
else:
    nagyobb = masodik+1
    kisebb = elso
for i in range (kisebb, nagyobb, lepeskoz):
    print (i)
print (" ")
print ("vagy")
print (" ")
a= int(input("a= "))
b= int(input("b= "))
c= int(input("c= "))
kicsi = min(a,b)
nagy= max(a,b)
for i in range (kicsi, nagy+1, c):
    print(i, end=" ")
print(" ")