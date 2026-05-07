pack = int(input("Enter the number of packages in a day: "))
drivers = int(input("Enter the number of drivers available: "))
money = int(input("Enter the amount of monthly salary for each driver: "))
trzby = pack * 30 * 2.50
naklady = drivers * money

if trzby > naklady:
    print(f"you made a profit of {trzby - naklady}")
elif naklady > trzby:
    print(f"you made a loss of {naklady - trzby}")
else:    print("you are even")