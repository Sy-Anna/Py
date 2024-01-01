import math

class Negyzet:
    neve=""
    a=0
    ker=0
    ter=0
    atlo=0
    mag=0

    def __init__(self, neve, a):
        self.a=a
        self.neve=neve

    def kerulete(self):
        return self.a*4
        
    def terulete(self):
        return self.a*self.a
    
    def atloja(self):
        return math.sqrt(2)*self.a
    
    def magassaga(self):
        return self.a
    
negyzetek=[]

def uj_negyzetek():
     negyzetek.append(Negyzet("négyzet1", 5))
     negyzetek.append(Negyzet("négyzet2",3))
     negyzetek.append(Negyzet("négyzet3",36))
     negyzetek.append(Negyzet("négyzet4",128))
     negyzetek.append(Negyzet("négyzet5",682))
        
def nyomtatni():
    for item in (negyzetek):
        print(f"{item.neve} a oldala {item.a} cm, kerülete {item.kerulete()} cm, területe {item.terulete()} cm2, átlója {item.atloja()} cm, magassága {item.magassaga()} cm.")

def main():
    uj_negyzetek()
    nyomtatni()

main()