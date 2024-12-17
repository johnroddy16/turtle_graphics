#!/usr/bin/env python3 

# we will write the random walk a slightly different way with less code:

import turtle as t  
import random 

alex = t.Turtle()
alex.pensize(10)  # larger pen size 
alex.speed(0)  # 0 is the fastest speed, could also write 'fastest' 

# colors = ['BlueViolet', 'powder blue', 'cadet blue', 'chartreuse', 'dark slate gray', 'DarkSeaGreen', 'DeepPink2', 'coral4', 'LightCyan1', 'LightGreen',
#           'LightSkyBlue2', 'medium spring green', 'MediumOrchid3', 'PaleGreen']  # leave the colors the same 4 now 

# Set color mode to RGB
t.colormode(255)

# changing the way we create random colors with a function that returns r, g, b tuple:
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

directions = [0, 90, 180, 270]  # 0 east, 90 north, 180 west, 270 south

for _ in range(1000):
    alex.color(random_color()) 
    alex.setheading(random.choice(directions))
    alex.forward(20)





screen = t.Screen()
screen.title('random walk')
screen.bgcolor('skyblue')
screen.exitonclick()