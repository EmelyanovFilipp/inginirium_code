import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win, bg='#000000', width=400, height=400)
for i in range(8):
    canvas.create_line((50*i,0),(50*i,400), fill="#FFFFFF")
    canvas.create_line((0,50*i),(400,50*i), fill="#FFFFFF")
for i in range(8):
    for j in range(3):
        if (i+j) % 2 == 0:
            canvas.create_oval((i*50,j*50),(50*(i+1),(j+1)*50), fill='#FFFFFF',)
    for j in range(5,8):
        if (i+j) % 2 == 0:
            canvas.create_oval((i*50,j*50),(50*(i+1),(j+1)*50), fill='blue')


canvas.pack()
win.mainloop()
