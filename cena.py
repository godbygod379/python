kg = float(input("how much does it weigh? "))
cm = float(input("how long is it? "))
price = float(input("how much does it cost? "))
final_price = 0
if kg <= 1:
    price = price + 3.20
elif kg <= 5:
    price = price + 4.80
elif kg <= 20:
    price = price + 7.90
else:
    price = price + 12.50

if cm > 80:
    price = price + 3.00
if price > 1000:
    price = price +0.03 * price
elif price > 500:
    price = price + 0.02 * price
elif price > 100:
    price = price + 0.01 * price

print(f"The final price is: {price}")