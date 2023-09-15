szelesseg = float(input("Adja meg a szoba szélességét: "))
hosszusag = float(input("Adja meg a szoba hosszúságát: "))
terulet = (2*hosszusag*1.5+2*szelesseg*1.5+hosszusag*szelesseg)*1.1
print(f"Ebben az esetben", round(terulet/1.44), "csomag csempére van szükség.")