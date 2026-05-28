x = int(input("Enter a number: "))
x *= 2
m = x
h = 0
for i in range (1, x, 2):
    if h == 0:
        print(" " * (m + 1) + "#" * i)
        h += 1
    print(" " * m + "#" +"-" * i + "#")
    m -= 1
print(" " * m + "#" * (x + 3))