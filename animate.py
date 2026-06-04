import tkinter
import random

c = tkinter.Canvas(width=1920, height=1080)
c.pack()
for i in range(100):
    x = random.randint(0, 1920)
    y = random.randint(0, 1080)
    sirka = random.randint(20, 100)
    vyska = random.randint(20, 100)
    r = random.randit(0, 255)
    g = random.randit(0, 255)
    b = random.randit(0, 255)
    color = f"#{r:02x}{g:02x}{b:02x}"
    c.create_rectangle(x, y, x + sirka, y + vyska, outline=color, fill=color)  

    c.after(100)
    c.update()


c.mainloop()