item = input("Enter the number id of the item you want to buy: ")
amount = int(input("Enter the amount you want to buy: "))
price = 0
if item == "0":\
    price = 51*amount
elif item == "1":
    price = 30*amount
elif item == "2":
    price = 215*amount
elif item == "3":
    price = 24*amount

if price >= 150:
    price = price * 0.9
print(f"The total price is: {price}€")