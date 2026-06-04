import tkinter
import random

c = tkinter.Canvas(width=800, height=600)
c.pack()

c.create_rectangle(random.randint(0, 800), random.randint(0, 600), random.randint(0, 800), random.randint(0, 600), fill="black")  


c.mainloop()