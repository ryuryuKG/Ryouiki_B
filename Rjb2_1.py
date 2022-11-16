import tkinter as tk
root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root, background="#fff", width=600, height=600)
canvas.pack()

def car_create(x_1,y_1,collar):
    canvas.create_rectangle(x_1, y_1, x_1*3, y_1*2, fill=collar)
    canvas.create_rectangle(x_1/2, y_1*2,  x_1*3.5, y_1*3, fill=collar)
    canvas.create_oval(x_1, y_1*3, x_1*1.5, y_1*3.5, fill="black")
    canvas.create_oval(x_1*2.5, y_1*3, x_1*3, y_1*3.5, fill="black")

car_create(10,10,"red")
car_create(50,50,"blue")
root.mainloop()