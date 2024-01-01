

class Kutyák:
    fajta=""
    nev=""
    kor=0
    nem=""
    suly=0

    def __init__(self, fajta, nev, kor, nem, suly):
        self.fajta=fajta
        self.nev=nev
        self.kor=kor
        self.nem=nem
        self.suly=suly

    def __str__(self) -> str:
         return f"{self.fajta} {self.nev} {self.kor} {self.nem} {self.suly}"

autok=[]

def uj_autok():
    autok.append(Kutyák("Bernáthegyi", "Vau", 5, "lány", 50))
    autok.append(Kutyák("Ujfullandi", "Pizsu", 8, "fiú", 63))
    autok.append(Kutyák("Sitzu", "Lea", 3, "lány", 3))
    autok.append(Kutyák("Boxer", "Furi", 12, "fiú", 4))
    autok.append(Kutyák("Macska", "Csöves", 4, "fiú", 5))
    print(*autok, sep= "\n")

uj_autok()