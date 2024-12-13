#!/usr/bin/env python3 

from turtle import Turtle as t, Screen as s 

mike = t()
mike.shape('turtle')
mike.color('blue')
screen = s()
width = screen.window_width() 
mike.penup()
mike.goto(-width/2, 0)

for _ in range(50):
    mike.pendown()
    mike.forward(10)
    mike.penup()
    mike.forward(10)










screen.exitonclick()