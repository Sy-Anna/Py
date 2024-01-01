#összetartozó adatokat együtt kezelünk - oop objektum orientált programozás
#objektumok: 
#class: sablon, tudjuk, hogy milyen tulajdonságokkal, metódusokkal rendelkezik az osztály
#Az objektum konkrét értékkel feltöltött példány
#osztály neve MINDIG nagybetűvel kezdődik
#Teve szabély: minden szó nagybetűvel kezdődik, kisbetűvel végződik, akkor is ha végig nagybetűs
class Szemely:
    #tulajdonságok: adattag, field, osztályváltozó - mérhető dolgok
    #név, életkor, magasság, lábszag, születési dátum, tömeg
    #képességek: metódusok, 
    #evés, fürdés, sportolás
    nev=""
    eletkor=0
    magassag=0
    tomeg=0

    def __init__(self, nev, eletkor, magassag, tomeg) -> None:
         self.nev=nev
         self.eletkor=eletkor
         self.magassag=magassag
         self.tomeg=tomeg

    def eves(self, mennyiseg):
        self.tomeg+=mennyiseg
    def sportolas(self, mennyiseg):
        if self.tomeg-mennyiseg>1:
            self.tomeg-=mennyiseg
    """def furdes():
        tomeg-=1"""
    def __str__(self) -> str:
         return f""
    
def peldanyositas():
        joska=Szemely()
        print(joska.nev)
        print(joska.eletkor)

def peldanyositas_inten_keresztül():
     joska=Szemely("Jóska", 58, 175, 75.2)
     print(joska.nev)
     print(joska.eletkor)
     print(joska.tomeg)
     bozsi=Szemely("Bözsi", 79, 200, 102)
     print(f"Jóska felesége {bozsi.nev}, {bozsi.eletkor} éves, {bozsi.magassag} magas, {bozsi.tomeg} kg.")
    
szemelyek=[]
def falu():
     szemelyek.append(Szemely("Jóska", 58, 175.2, 91))
     szemelyek.append(Szemely("Bözsi", 79, 102, 200))
     szemelyek.append(Szemely("Bíró", 63, 184, 79))
     szemelyek.append(Szemely("Bíróné", 66, 162, 80))
     szemelyek.append(Szemely("Marcika", 21, 170, 60))
     print(*szemelyek, sep= "\n")
     print("-----------------------------")
     for item in szemelyek:
          print(f"{item.nev}, {item.eletkor}")

def main():
    #peldanyositas()
    peldanyositas_inten_keresztül()

main()