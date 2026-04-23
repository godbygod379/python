s = int(input("Zadaj pocet sekund: "))
hour = s // 3600
minute = (s % 3600) // 60
second = s % 60 
print(f"{hour}:{minute}:{second}")
