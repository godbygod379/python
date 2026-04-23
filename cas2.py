s = int(input("Zadaj pocet sekund: "))
h = s // 3600
m = (s % 3600) // 60
sec = s % 60
print(f"{s} sekund je {h} hodin, {m} minut a {sec} sekund.")
