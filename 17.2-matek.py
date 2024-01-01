class MathOperations:
    osszeadas=0
    kivonas=0
    szorzas=0
    osztas=0
    szam1=0
    szam2=0

    def __init__(self, szam1, szam2) -> None:
        self.szam1=szam1
        self.szam2=szam2

    def osszeadas(self):
        return self.szam1+self.szam2

    def kivonas(self):
        return self.szam1-self.szam2
    
    def szorzas(self):
        return self.szam1*self.szam2
    
    def osztas(self):
        return self.szam1/self.szam2

def peldanyositas():
    szamok=MathOperations(5,8)
    print(f"{szamok.szam1}+{szamok.szam2}={szamok.osszeadas()}")
    print(f"{szamok.szam1}-{szamok.szam2}={szamok.kivonas()}")
    print(f"{szamok.szam1}*{szamok.szam2}={szamok.szorzas()}")
    print(f"{szamok.szam1}/{szamok.szam2}={szamok.osztas()}")


def main():
    peldanyositas()

main()