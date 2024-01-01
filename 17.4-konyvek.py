class Book:
    cim=""
    szerzo=""
    datum=0

    def __init__(self, cim, szerzo, datum) -> None:
        self.cim=cim
        self.szerzo=szerzo
        self.datum=datum
    def __str__(self) -> str:
        return f"{self.cim}, {self.szerzo}, {self.datum}"
    
konyvek=[]
def peldanyositas():
    konyvek.append(Book("Édes Anna" , "Kosztolányi Dezső", "1926"))
    konyvek.append(Book("Az ember tragédiája" , "Madách Imre", "1969"))
    konyvek.append(Book("Nem baj, majd megértem" , "Bodor Johanna", "2014"))
    konyvek.append(Book("Tóthék" , "Örkény István", "1966"))

def nyomtatni():
    for item in konyvek:
        print (item)

def main():
    peldanyositas()
    nyomtatni()

main()