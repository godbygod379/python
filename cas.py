hodiny = int(input("Zadajte hodiny: "))
minuty = int(input("Zadajte minuty: "))
sekundy = int(input("Zadajte sekundy: "))
celkovo_sekund = hodiny * 3600 + minuty * 60 + sekundy
print(f"Celkovo sekund: {celkovo_sekund}")