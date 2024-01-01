import random
megoldasok = ["marcipán", "keserű", "zeller", "macska", "seprűnyél", "csokoládé", "hegedű", "mosoly", "csincsilla", "giliszta", "garnéla", "selyem", "sütemény", "trapéz", "zokni"]
szo = random.choice(megoldasok)
#print("debug: "+szo)
#print(" ")
elet = 5
talalatok = []
for betu in szo:
  talalatok.append("_")
fut_a_jatek = True

while fut_a_jatek:

  kiiratas = " ".join(talalatok)
  print(kiiratas)
  print(" ")
  print("Életek száma: " + str(elet))
  print(" ")
  tipp = input("Adj meg egy új tippet: ")
  talalt_jo_betut = False
  szam=0
  for betu in szo:
    if tipp == betu:
      talalatok[szam] = betu
      talalt_jo_betut = True
    szam = szam+1
  if talalt_jo_betut == False:
    print(" ")
    print(" ")
    print("Sajnos nem jó :(")
  else:
    print(" ")
    print("Eltaláltad, ügyes vagy! :)")
  print(" ")
  print("-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-")
  print(" ")
  #print("debug: " + str(talalt_jo_betut))
  
  if talalt_jo_betut == False:
    elet= elet - 1
  if elet == 0:
    print("game over :(")
    fut_a_jatek = False
  if "_" not in talalatok:
    print("nyertél!!4!")
    fut_a_jatek = False