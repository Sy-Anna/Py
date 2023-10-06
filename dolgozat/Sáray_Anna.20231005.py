import math

print("")
print("1. feladat")
print("")

for i in range (-10, 26):
    print(i, end=" ")
print()

print("")
print("2. feladat")
print("")

for i in range (75, 30, -3):
    print(i, end=" ")
print()

print("")
print("3. feladat")
print("")

a = float(input("a= "))
b = float(input("b= "))
if a < b :
    kisebb = a
    nagyobb = b
else:
    kisebb = b
    nagyobb = a
c = math.floor(7.25)
print(c)
kisebb = math.floor(kisebb)
nagyobb = math.ceil(nagyobb)
print(f"Kisebb egész szám = {kisebb}")
print(f"Nagyobb egész szám = {nagyobb}")
for i in range (kisebb, nagyobb, 2):
    print(i, end=", ")