rok = int(input("Enter a year: "))
if rok % 4 == 0:
    print("The year is a leap year.")
elif rok % 100 == 0:
    print("The year is not a leap year.")
elif rok % 400 == 0:
    print("The year is a leap year.")
else: print("error")