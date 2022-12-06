import tkinter as tk
import time
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

def id_input(id_num):
    if int(id_num)>=0 and int(id_num)<100:
        for j in range(len(car_l)):
            if (int(car_l[j].id) == int(id_num)):
                del car_l[int(j)]
                break
        canvas.delete("all")
        for i in range(len(car_l)):
            car_create(car_l[i].x_l, car_l[i].y_l, car_l[i].size, car_l[i].color)
    else:
        print("0から99までの数値を入力してください")
        #return id_input(input("idを入力してください:"))
_input=False
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
while True:
    root.update()
    time.sleep(0.02)
    _id=input("idを入力してください:")
    if bool(_id):
        id_input(_id)
