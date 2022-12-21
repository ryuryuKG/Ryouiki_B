import math
import tkinter as tk
import time
import numpy as np
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
    car_pos=np.array([0,0])
    def car_create(self,x_l, y_l, size, color):
        self.car_front=canvas.create_rectangle(10 * size + x_l, 10 * size + y_l, 30 * size + x_l, 20 * size + y_l, fill=color)
        self.car_body=canvas.create_rectangle(5 * size + x_l, 20 * size + y_l, 35 * size + x_l, 30 * size + y_l, fill=color)
        self.car_wheel_right=canvas.create_oval(10 * size + x_l, 30 * size + y_l, 15 * size + x_l, 35 * size + y_l, fill="black")
        self.car_wheel_left=canvas.create_oval(25 * size + x_l, 30 * size + y_l, 30 * size + x_l, 35 * size + y_l, fill="black")
        pos_f = canvas.bbox(self.car_front)
        pos_b = canvas.bbox(self.car_body)
        self.car_pos[0]=(pos_b[2]+pos_b[0])/2
        self.car_pos[1]=(pos_b[3]+pos_f[1])/2
    def car_del(self):
        canvas.delete(self.car_front)
        canvas.delete(self.car_body)
        canvas.delete(self.car_wheel_left)
        canvas.delete(self.car_wheel_right)
    def car_move(self,x_move,y_move):
        canvas.move(self.car_front, x_move, y_move)
        canvas.move(self.car_body, x_move, y_move)
        canvas.move(self.car_wheel_left, x_move, y_move)
        canvas.move(self.car_wheel_right, x_move, y_move)
        self.car_pos[0]+=x_move
        self.car_pos[1]+=y_move

class  Cannon(object):
    cannon_front = None
    cannon_body = None
    cannon_pos=np.array([0,0])
    def cannon_create(self,x_l, y_l, size):
        self.cannon_front=canvas.create_rectangle(15 * size + x_l, 10 * size + y_l, 25 * size + x_l, 20 * size + y_l, fill=self.color)
        self.cannon_body=canvas.create_rectangle(5 * size + x_l, 20 * size + y_l, 35 * size + x_l, 30 * size + y_l, fill=self.color)
        cannon_pos_f = canvas.bbox(self.cannon_front)
        cannon_pos_b = canvas.bbox(self.cannon_body)
        self.cannon_pos[0]= (cannon_pos_b[2] + cannon_pos_b[0])/2
        self.cannon_pos[1] = (cannon_pos_b[3] + cannon_pos_f[1])/2

class Cannon_ball(object):
    ball=None
    ball_pos=np.array([None,None])

    def cannon_ball_create(self):
        self.ball=canvas.create_oval(15 * self.size + self.x_l, 10 * self.size + self.y_l-50, 25 * self.size + self.x_l, 20 * self.size + self.y_l-50, fill=self.color)
        pos = canvas.bbox(self.ball)
        self.ball_pos[0]=(pos[2]+pos[0])/2
        self.ball_pos[1]=(pos[3]+pos[1])/2
    def cannon_ball_move(self):
        canvas.move(self.ball, 0, -10)
        self.ball_pos[0] += 0
        self.ball_pos[1] += -10
    def cannon_ball_del(self):
        canvas.delete(self.ball)


root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root, background="#fff", width=600, height=600)
canvas.pack()


_car=Car(1, 50 * 0, 50 * 1, 1, "blue")
_car.car_create(_car.x_l, _car.y_l, _car.size, _car.color)
count = 0

upd=True

cannon1=Cannon(1, 50 * 4, 50 * 8, 3,"green")
cannon1.cannon_create(cannon1.x_l, cannon1.y_l, cannon1.size)
cannon_balls=[]
speed=10
nowpos=0
def cannon_burst(event):
    cannon_balls.append(Cannon_ball(1,50 * 4, 50 * 8, 3,"black"))
    cannon_balls[-1].cannon_ball_create()
while True:
    root.bind('<Key-c>', cannon_burst)
    try:
        _car.car_move(speed, 0)
        nowpos=nowpos+speed
        if nowpos==600:
            speed=-10
        if nowpos==0:
            speed=10
    except NameError as e:
        pass
    for num_ball in range(len(cannon_balls)):
        cannon_balls[num_ball].cannon_ball_move()

    for j in range(len(cannon_balls)):
        print(np.linalg.norm(cannon_balls[j].ball_pos - _car.car_pos))
        if np.linalg.norm(cannon_balls[j].ball_pos - _car.car_pos) <= 80:
            _car.car_del()
            del _car
            _car = Car(1, 50 * 0, 50 * 1, 1, "blue")
            _car.car_create(_car.x_l, _car.y_l, _car.size, _car.color)
            _car.car_pos = np.array([0, 0])
            speed=10
            nowpos=0

    for i in range(len(cannon_balls)):
        try:
            if cannon_balls[i].ball_pos[1] <= -500:
                cannon_balls[i].cannon_ball_del()
                del cannon_balls[i]
        except IndexError as e:
            pass
    #print(len(cannon_balls))
    time.sleep(0.02)
    root.update()
