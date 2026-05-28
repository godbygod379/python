import tkinter

c = tkinter.Canvas(width=800, height=600)
c.pack()

c.create_rectangle(350, 420, 370, 520, fill="black")  
c.create_rectangle(430, 420, 450, 520, fill="black")  
c.create_rectangle(320, 220, 480, 420, fill="lightgray", outline="lightgray")
c.create_oval(340, 100, 460, 220, fill="blue", outline="blue")



c.mainloop()