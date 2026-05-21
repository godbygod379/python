import random


pos = 1
rolls = 0

while pos != 100:
    rolls += 1
    die = random.randint(1, 6)
    pos += die

    if pos > 100:
        pos = 100 - (pos - 100)

    if pos == 8:
        pos = 14
    elif pos == 25:
        pos = 55
    elif pos == 40:
        pos = 64
    elif pos == 75:
        pos = 97
    elif pos == 37:
        pos = 3
    elif pos == 66:
        pos = 33
    elif pos == 92:
        pos = 28
    elif pos == 98:
        pos = 61
    wait(5)

    print(f"Si na policku {pos}, hodil si cislo {die}")

print(f"Vyhral si, kockou si musel hadzat {rolls} krat")
