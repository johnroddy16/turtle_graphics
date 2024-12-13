#!/usr/bin/env python3 

from turtle import Turtle as t, Screen as s
import random 

 

john = t()
john.shape('turtle')

colors = ['blue', 'green', 'purple', 'magenta', 'pink', 'alice blue', 'chartreuse4', 'dark cyan']

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        john.forward(100)
        john.right(angle)
        
for shape_side_n in range(3, 11):
    color = random.choice(colors)
    colors.remove(color)
    john.color(color)
    draw_shape(shape_side_n) 











screen = s()
screen.exitonclick() 