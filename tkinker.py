import tkinter

c = tkinter.Canvas(width=800, height=600)
c.pack()

c.create_rectangle(350, 420, 370, 520, fill="black")  
c.create_rectangle(430, 420, 450, 520, fill="black") 

c.create_rectangle(320, 220, 480, 420, fill="lightgray", outline="lightgray")

c.create_oval(340, 100, 460, 220, fill="blue", outline="blue")

c.create_rectangle(360, 140, 440, 180, fill="orange", outline="orange")
c.create_rectangle(370, 148, 430, 172, fill="yellow", outline="yellow")

c.create_polygon(400, 20, 370, 110, 430, 110, fill="purple", outline="purple")


c.mainloop()