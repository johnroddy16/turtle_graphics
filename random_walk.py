#!/usr/bin/env python3 

# using the tirtle module to create a random walk as i originally wrote the code: 

from turtle import Turtle as t, Screen as s 
import random 

alex = t()
alex.pensize(5)
alex.speed(0)
colors = ['BlueViolet', 'brown4', 'cadet blue', 'chartreuse', 'dark slate gray', 'DarkSeaGreen', 'DeepPink2', 'coral4']
directions = [0, 1]  # 0 for left and 1 for right 
angles = [90, 180, 360]



for _ in range(1000):
    alex.color(random.choice(colors))
    alex.forward(20)
    direction = random.choice(directions)
    if direction == 0:
        alex.left(random.choice(angles))
    else:
        alex.right(random.choice(angles))




screen = s()
screen.exitonclick() 