import tkinter as tk

class Car:
    def __init__(self,id, x_l, y_l,size,color):
        self.id=id
        self.x_l = x_l
        self.y_l =y_l
        self.size=size
        self.color=color

def car_create(x_l, y_l, size, color):
    canvas.create_rectangle(10 * size + x_l, 10 * size + y_l, 30 * size + x_l, 20 * size + y_l, fill=color)
    canvas.create_rectangle(5 * size + x_l, 20 * size + y_l, 35 * size + x_l, 30 * size + y_l, fill=color)
    canvas.create_oval(10 * size + x_l, 30 * size + y_l, 15 * size + x_l, 35 * size + y_l, fill="black")
    canvas.create_oval(25 * size + x_l, 30 * size + y_l, 30 * size + x_l, 35 * size + y_l, fill="black")

def car_del(x_l, y_l, size, color):
    canvas.delete(canvas.create_rectangle(10 * size + x_l, 10 * size + y_l, 30 * size + x_l, 20 * size + y_l, fill=color))
    canvas.delete(canvas.create_rectangle(5 * size + x_l, 20 * size + y_l, 35 * size + x_l, 30 * size + y_l, fill=color))
    canvas.delete(canvas.create_oval(10 * size + x_l, 30 * size + y_l, 15 * size + x_l, 35 * size + y_l, fill="black"))
    canvas.delete(canvas.create_oval(25 * size + x_l, 30 * size + y_l, 30 * size + x_l, 35 * size + y_l, fill="black"))

def id_input(event):
    id_num = input("idを入力してください:")
    for j in range(len(car_l)):
        if(int(car_l[j].id)==int(id_num)):
            del car_l[int(j)]
            break
    canvas.delete("all")
    for i in range(len(car_l)):
        car_create(car_l[i].x_l, car_l[i].y_l, car_l[i].size, car_l[i].color)
    #root.update()

root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root, background="#fff", width=600, height=600)
canvas.pack()
car_l=[]
num=0
id=0
for i in range(10):
    num=0
    for j in range(10):
        if i%2==0:
            if num%2==0:
                car_l.append(Car(id, 50 * j, 50 * i, 1, "red"))
            else:
                car_l.append(Car(id, 50 * j, 50 * i, 1, "blue"))
        else:
            if num%2==0:
                car_l.append(Car(id, 50 * j, 50 * i, 1, "blue"))
            else:
                car_l.append(Car(id, 50 * j, 50 * i, 1, "red"))
        num=num+1
        id=id+1

for i in range(len(car_l)):
    car_create(car_l[i].x_l, car_l[i].y_l, car_l[i].size, car_l[i].color)
root.bind('<Button-1>',id_input)

root.mainloop()
