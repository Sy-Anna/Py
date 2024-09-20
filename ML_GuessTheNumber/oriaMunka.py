import random

def setting():
    gm=int(input("Válassz skálát: 1, 2, 3"))
    while True:
        if gm==1 or gm==2 or gm==3:
            if gm==1:
                last=10
            if gm==2:
                last=100
            if gm==3:
                last=1000
            break
        else:
            gm=int(input("Nem jó, válassz a z1, 2, 3 közül!"))
    gessNum=int(input("Add meg a tippek számát! 1, 2, 3"))
    while True:
        if gessNum==1 or gessNum2==2 or gessNum==3:
            if gessNum==1:
                guessLeft=-1
            if guessNum==2:
                guessLeft=10
            if guessNum==3:
                guessLeft=3
            break
        else:
            gm=int(input("Nem jó, válassz a z1, 2, 3 közül!"))
    return last, guessLeft

def game(last, guessLeft):
    print("Kezdődik a játék!")
    megfejtes=random.randint(1,last)
    while guessLeft<0 or guessLeft>0:
        tipp=input("x-el kilépsz, adj meg tippet!")
        if tipp == x:
            print("kiléptél!")
            break
        elif int(tipp)==megfejtes:
            print("Nyertél!")
            break
        else:
            print("Nem jó tipp!")
            guessLeft-=1

def main():
    setup=setting()
    last=setup[0]
    gessLeft=setup[1]
    game(last, guessLeft)

main()
