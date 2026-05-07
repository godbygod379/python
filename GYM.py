perm = float(input("Enter the price for a permanent membership: "))
temp = float(input("Enter the price for a temporary membership: "))
times = int(input("Enter the number of times you want to use the gym: "))
gaga = temp * times
if gaga < perm:
    print(f"You are losing {perm - gaga} dollars by buying a permanent membership.")
elif gaga > perm:
    print(f"You are saving {gaga - perm} dollars by buying a permanent membership.")
else: print("It doesnt matter.")
