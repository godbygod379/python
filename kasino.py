import random
money = int(input("How much money do you have? "))
bet = int(input("How much do you want to bet? "))
lost = 0
go = 1
while bet > money and go == 1:
    print("You don't have enough money to bet that amount.")
else:
    choose = input("Choose a number between 0 and 10: ")
    print("Bet placed.")
    money = money - bet
    print("Spinning the wheel...")
    result = random.randint(0, 10)
    if result == choose:
        print("Congratulations! You won!")
        money = bet * 2
    else:
        print("Sorry, you lost.")
        lost = lost + bet
        money = money - bet
    go = int(input("Do you want to play again? (1 for yes, 0 for no) "))
    if money > 0:
        print(f"your balance is {money}")
print(f"You have {money} left.")
