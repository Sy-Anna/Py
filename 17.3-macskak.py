class Cat:
    neve=""
    elete=0

    def __init__(self, neve, elete) -> None:
        self.neve=neve
        self.elete=elete
    
    def __str__(self) -> str:
        return f"{self.neve}"
    
macskak=[]
def peldanyositas():
    macskak.append(Cat("Cirmi", 9))
    macskak.append(Cat("Csöves", 9)) #sajátom, és igazából két otthona is van...
    macskak.append(Cat("Gyökér", 9)) #ő róla csak hallottam
    macskak.append(Cat("Anubis", 9))
    macskak.append(Cat("Mau", 9))

def halal():
    while True:
        cica=str(input("Melyik macska élete csökkent?"))
        found=0
        for item in macskak:
            if cica==item.neve:
                found+=1
                item.elete-=1
                print(f"{item.neve} cica életeinek száma {item.elete}.")
                if item.elete==0:
                    print(f"{item.neve} sajnos meghalt :'(")
        if found==0:
            print("Nincs ilyen nevű macska!")
        valasz=input("Ki akar lépni? (i/n)")
        if valasz == "i":
            break
        

def nyomtatni():
    for item in macskak:
        print(f"{item.neve} cica életeinek száma {item.elete}.")

def main():
    nyomtatni()
    peldanyositas()
    halal()
    nyomtatni()

main()