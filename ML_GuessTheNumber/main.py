import random

def settings():
    gm=int(input("Válassz játékmódot!\n1: 1-től 10-ig , 2: 1-től 100-ig, 3: 1-től 1000-ig\n"))
    while True:
        if gm == 1 or gm == 2 or gm == 3:
            if gm == 1:
                lastNum=10
            elif gm == 2:
                lastNum=100
            elif gm == 3:
                lastNum=1000
            break
        else:
            gm=int(input("\nNem jó válasz! Az alábbi számok közül válassz: 1, 2, 3\n"))
    guessNum=int(input("\nVálassz nehézségi szintet!\n1: végtelen tipp, 2: 10 tipp, 3: 3 tipp, 4: szabadon beállítható\n"))
    while True:
        if guessNum == 1 or guessNum == 2 or guessNum == 3 or guessNum == 4:
            if guessNum == 1:
                guessesLeft = -1
            elif guessNum == 2:
                guessesLeft=10
            elif guessNum == 3:
                guessesLeft=3
            elif guessNum == 4:
                guessesLeft=int(input("\nAdd meg, hány tipp lehetőséget szeretnél: "))
            break
        else:
            guessNum=int(input("\nNem jó válasz! Az alábbi számok közül válassz: 1, 2, 3, 4\n"))
    
    return gm, lastNum, guessesLeft

def checkWin(lastNum, guessesLeft):
    print("\n\n-=Kezdődik a játék=-")
    num=random.randint(1, lastNum)
    while guessesLeft > 0 or guessesLeft < 0:
        guess=input("\nKilépéshez nyomj x-et!\nAdj meg egy tippet: ")
        if guess == "x":
            print("\nKiléptél a játékból.")
            break
        elif int(guess) == num:
            print("\nGratulálok, eltaláltad :D")
            break
        else:
            print("\nSajnos nem talált :(")
        guessesLeft-=1

def main():
    setup=settings()
    lastNum=setup[1]
    guessesLeft=setup[2]
    checkWin(lastNum, guessesLeft)

main()
