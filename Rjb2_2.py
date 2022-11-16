import tkinter as tk
root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root, background="#fff", width=600, height=600)
canvas.pack()
def car_create(x_l,y_l,size,collar):
    canvas.create_rectangle(10*size+x_l, 10*size+y_l, 30*size+x_l, 20*size+y_l, fill=collar)
    canvas.create_rectangle(5*size+x_l, 20*size+y_l, 35*size+x_l, 30*size+y_l, fill=collar)
    canvas.create_oval(10*size+x_l, 30*size+y_l, 15*size+x_l, 35*size+y_l, fill="black")
    canvas.create_oval(25*size+x_l, 30*size+y_l, 30*size+x_l, 35*size+y_l, fill="black")
for i in range(10):
    num=0
    for j in range(10):
        if i%2==0:
            if num%2==0:
                car_create(50*j, 50*i, 1, "red")
            else:
                car_create(50 * j, 50 * i, 1, "blue")
        else:
            if num%2==0:
                car_create(50*j, 50*i, 1, "blue")
            else:
                car_create(50 * j, 50 * i, 1, "red")
        num=num+1
root.mainloop()