import random
import os

# Generate a random number between 1 and 5
secret_number = random.randint(1, 5)

# Ask user to guess
try:
    guess = int(input("Guess a number between 1 and 5: "))
    
    if guess == secret_number:
        print("You won! Nothing happens.")
    else:
        print("Wrong guess! Shutting down...")
        os.system("shutdown /s /t 5")
except ValueError:
    print("Please enter a valid number!")
    os.system("shutdown /s /t 5")
