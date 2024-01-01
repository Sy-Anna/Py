

class Media:
    cim=""
    eloado=""
    megy=0

    def __init__(self, cim, eloado, megy):
        self.cim=cim
        self.eloado=eloado
        self.megy=megy
    
    def __str__(self) -> str:
        return f"{self.cim} {self.eloado} {self.megy}"

zenek=[]

def peldanyositas():
    zenek.append(Media("Tamino", "Habibi", 0))
    zenek.append(Media("It happened quiet", "Aurora", 0))
    zenek.append(Media("Like real people do", "Hozier", 0))
    zenek.append(Media("Space odity", "Dawid Bowie", 0))
    zenek.append(Media("No surprises", "Radiohead", 0))
    zenek.append(Media("Uprising", "Muse", 0))

def kiiratas():
    for item in zenek:
        print(f"{item.eloado}: {item.cim}")

def start():
    for item in zenek:
        print()
        valasz = str(input(f"El akarja indítani a {item.cim} című zenét {item.eloado}-tól/től? (i/n)"))
        if valasz=="i":
            item.megy=1
            input("Megállítja a zenét? (enter)")
        else:
            item.megy=0
    print("A lejátszási lista végigment!")

def main():
    peldanyositas()
    kiiratas()
    start()

main()