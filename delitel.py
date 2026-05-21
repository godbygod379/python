n = int(input("Zadej číslo: "))
spolu = 0
pocet = 0
for delitel in range(1, n + 1):
    if n % delitel == 0:
        spolu += delitel
        pocet += 1
        print(delitel)
print(f"Počet dělitelů čísla {n}: {spolu}")