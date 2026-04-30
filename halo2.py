mat = int(input("Enter the grade from math: "))
sjl = int(input("Enter the grade from Slovakias language: "))
fyz = int(input("Enter the grade from physics: "))
bio = int(input("Enter the grade from biology: "))
print("Dostaneš")
presents = 3 
if mat == 1 and sjl < 3:
    print("bicykel")
else: presents = presents - 1

if fyz == 1 or bio == 1:
    print("tričko")
else: presents = presents - 1

if (mat+sjl+fyz+bio)/4 <= 1:
    print("ponožky")
else: presents = presents - 1

if presents == 0:
    print("nic")
    presents = 3

