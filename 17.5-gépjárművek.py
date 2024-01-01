class Vehicle:
    rendszam=""
    pozicio=""

    def __init__(self, rendzsam, pozicio) -> None:
        self.rendszam=rendzsam
        self.pozicio=pozicio

    def __str__(self) -> str:
        return f"{self.rendszam} {self.pozicio}"
    
autok=[] 
def peldanyositas():
    autok.append(Vehicle("IED-321", "áll"))
    autok.append(Vehicle("NCJ-869", "megy"))

def nyomtatas():
    for item in autok:
        print(item)

def main():
    peldanyositas()
    nyomtatas()

main()