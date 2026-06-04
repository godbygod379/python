import tkinter
import random

c = tkinter.Canvas(width=800, height=600)
c.pack()
for i in range(100):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    sirka = random.randint(20, 100)
    vyska = random.randint(20, 100)
    c.create_rectangle(x, y, x + sirka, y + vyska, outline="black")  

    c.after(100)
    c.update()


c.mainloop()