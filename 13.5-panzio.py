panzio = [0]*12
print(*panzio)
#jönnek a vendégek. Ha a vendégek száma 0, kilépünk a ciklusból
def erkezes():
    while True:
        vendegszam = int(input("Hány vendég érkezett: "))
        if vendegszam == 0:
            break
        print("Szobakulcsok: ", end= "")
        while vendegszam>0:
            for i in range(len(panzio)):
                if panzio[i] == 0:
                    if vendegszam == 1:
                        panzio[i] =1
                        vendegszam-=1
                        print(f"{i+1}", end=" ")
                    elif vendegszam >= 2:
                        panzio[i] = 2    
                        vendegszam -=2
                        print(f"{i+1}", end=" ")
                    else:
                        break
            print()        
            if vendegszam>0:
                break
        if vendegszam>0:
                print(f"Nincs több szoba! {vendegszam} vendéget nem tudunk elszállásolni")
                break        
    print(*panzio)                    
def listazas():
    for i in range(len(panzio)):
        print(f"{i+1}. szoba: {panzio[i]}")



def torles():
    while True:
        szobaszam= int(input("Melyik szobábol szedretne kijelentkezni: "))
        if szobaszam< 1 or szobaszam> 12:
            print("Nincs ilyen szoba!")
        elif panzio[szobaszam-1] == 0:
            print("Ez a szoba üres, nem innen költözik ki :) ")
            listazas()
        else:
            panzio[szobaszam-1] = 0
            break 
    print("Köszönjük, hogy minket választott!")

def recepcio():
    while True:
        print("1. bejelentkezés\n2. kijelentkezes\n3.Listázás\n4. Vendégek száma\n5. Szilveszteri bevétel\n6. Bevételkiesés\n7. kilépés ")
        menu= int(input("Melyik menüt választja: "))
        if menu==7:
            break
        elif menu == 1:
            erkezes()
        elif menu== 2:
            torles()    
        elif menu == 3:
            listazas    

def main():
    recepcio()


main()    