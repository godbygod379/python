kg = float(input("how much does it weigh? "))
cm = float(input("how long is it? "))
price = float(input("how much does it cost? "))
final_price = 0
if kg <= 1:
    final_price = final_price + 3.20
elif kg <= 5:
    final_price = final_price + 4.80
elif kg <= 20:
    final_price = final_price + 7.90
else:
    final_price = final_price + 12.50

if cm > 80:
    final_price = final_price + 3.00
if price > 1000:
    final_price = final_price + 0.03 * price
elif price > 500:
    final_price = final_price + 0.02 * price
elif price > 100:
    final_price = final_price + 0.01 * price

print(f"The final price is: {final_price} euros")