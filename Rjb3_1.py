import math
import tkinter as tk
import time

class object:
    def __init__(self,id, x_l, y_l,size,color):
        self.id=id
        self.x_l = x_l
        self.y_l =y_l
        self.size=size
        self.color=color

class Car(object):
    car_front = None
    car_body = None
    car_wheel_right = None
    car_wheel_left = None
    def car_create(self,x_l, y_l, size, color):
        self.car_front=canvas.create_rectangle(10 * size + x_l, 10 * size + y_l, 30 * size + x_l, 20 * size + y_l, fill=color)
        self.car_body=canvas.create_rectangle(5 * size + x_l, 20 * size + y_l, 35 * size + x_l, 30 * size + y_l, fill=color)
        self.car_wheel_right=canvas.create_oval(10 * size + x_l, 30 * size + y_l, 15 * size + x_l, 35 * size + y_l, fill="black")
        self.car_wheel_left=canvas.create_oval(25 * size + x_l, 30 * size + y_l, 30 * size + x_l, 35 * size + y_l, fill="black")
    def car_del(self,car_front,car_body,car_wheel_right,car_wheel_left):
        canvas.delete(self.car_front)
        canvas.delete(self.car_body)
        canvas.delete(self.car_wheel_left)
        canvas.delete(self.car_wheel_right)
    def car_move(self,x_move,y_move):
        canvas.move(self.car_front, x_move, y_move)
        canvas.move(self.car_body, x_move, y_move)
        canvas.move(self.car_wheel_left, x_move, y_move)
        canvas.move(self.car_wheel_right, x_move, y_move)
root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root, background="#fff", width=600, height=600)
canvas.pack()
a=Car(1, 50 * 0, 50 * 1, 1, "blue")
a.car_create(a.x_l, a.y_l, a.size, a.color)
count = 0
while True:
    a.car_move(math.cos(math.radians(count))*10, 0)
    count+=1
    if(count > 180):
        count=0
    time.sleep(0.02)
    root.update()
