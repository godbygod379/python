import tkinter
import random

c = tkinter.Canvas(width=800, height=600)
c.pack()
for i in range(100):
    c.create_rectangle(random.randint(0, 800), random.randint(0, 600), random.randint(0, 800), random.randint(0, 600), outline="black")  


c.mainloop()