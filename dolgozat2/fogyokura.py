alomsuly = float(input("Hány kiló szeretne lenni Marinéni? "))
uj_suly=0
het=1
hizott=0
nyero_het=0
while True:
    regi_suly=uj_suly
    uj_suly=float(input(f"{het}. héten Mari néni súlya: "))
    if uj_suly>regi_suly:
        hizott+=1
    if uj_suly>=alomsuly:
        nyero_het+=1
    if uj_suly==0:
        break
    het+=1
if nyero_het>0:
    print(f"Marinéni a(z) {nyero_het}. héten elérte a célját.")
if hizott>0:
    print(f"A tömege {hizott-1} esetben nőtt.")