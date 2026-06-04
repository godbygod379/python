"""
import tkinter
import random

c = tkinter.Canvas(width=1920, height=1080)
c.pack()
for i in range(1000000):
    x = random.randint(0, 1920)
    y = random.randint(0, 1080)
    sirka = random.randint(20, 100)
    vyska = random.randint(20, 100)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color2 = f"#{(255 - r):02x}{(255 - g):02x}{(255 - b):02x}"
    color = f"#{r:02x}{g:02x}{b:02x}"
    c.create_rectangle(x, y, x + sirka, y + vyska, outline=color2, fill=color, width = 5)  

    c.after(1)
    c.update()


c.mainloop()
"""


import tkinter
import random
from turtle import width

x_krok = 5
y_krok = 5

x = 500
y = 250

c = tkinter.Canvas(width=1000, height=500)
c.pack()

for i in range(1000000):
    c.delete("all")
    c.create_rectangle(x, y, x + 50, y + 50, fill = "black", outline = "black")


    
    x += x_krok
    y += y_krok

    if x <= 0:
        x_krok = 5
        x += 5

    if y <= 0:
        y_krok = 5
        y += 5

    if x + 50 >= 1000:
        x_krok = -5
        x -= 5

    if y + 50 >= 500:
        y_krok = -5
        y -= 5

    c.after(1)
    c.update()





c.mainloop()