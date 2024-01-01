

class Autók:
    marka=""
    tipus=""
    evjarat=0
    ajtok=0

    def __init__(self, marka, tipus, evjarat, ajtok):
        self.marka=marka
        self.tipus=tipus
        self.evjarat=evjarat
        self.ajtok=ajtok

    def __str__(self) -> str:
         return f"{self.marka} {self.tipus} {self.evjarat} {self.ajtok}"

autok=[]

def uj_autok():
    autok.append(Autók("Honda", "Jazz", 2002, 5))
    autok.append(Autók("Honda", "Civic", 2005, 5))
    autok.append(Autók("Suzuki", "Swift", 2003, 5))
    autok.append(Autók("Suzuki", "Vitara", 2007, 5))
    autok.append(Autók("Tesla", "Model 3", 2019, 5))
    print(*autok, sep= "\n")

uj_autok()