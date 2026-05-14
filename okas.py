import random
otaz = int(input("How many times do you want to turn it? "))
lol = 0
kolko = 0
while otaz > 0:
    lol = random.randint(1, 6)
    if lol == 6:
        kolko += 1
    otaz -= 1
print(f"You rolled a 6, {kolko} times.")