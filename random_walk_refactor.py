#!/usr/bin/env python3 

# we will write the random walk a slightly different way with less code:

from turtle import Turtle as t, Screen as s 
import random 

alex = t()
alex.pensize(10)  # larger pen size 
alex.speed(0)  # 0 is the fastest speed, could also write 'fastest' 

colors = ['BlueViolet', 'powder blue', 'cadet blue', 'chartreuse', 'dark slate gray', 'DarkSeaGreen', 'DeepPink2', 'coral4', 'LightCyan1', 'LightGreen',
          'LightSkyBlue2', 'medium spring green', 'MediumOrchid3', 'PaleGreen']  # leave the colors the same 4 now 

directions = [0, 90, 180, 270]  # 0 east, 90 north, 180 west, 270 south

for _ in range(1000):
    alex.setheading(random.choice(directions))
    alex.color(random.choice(colors))
    alex.forward(20)





screen = s()
screen.title('random walk')
screen.bgcolor('skyblue')
screen.exitonclick()