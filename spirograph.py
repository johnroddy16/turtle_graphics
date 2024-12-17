#!/usr/bin/env python3 

# each circle should be of radius 100 

import turtle as t 
from random_walk_refactor import random_color

andy = t.Turtle()
andy.speed(0)  # change speed to fastest  
t.colormode(255)  # change color mode to rgb  

def main():
    draw_spirograph(4)  
    screen = t.Screen()
    screen.exitonclick() 
    screen.title('spirograph')  


# spirograph function:
def draw_spirograph(gap_size): 
    for _ in range(int(360/gap_size)):
        andy.color(random_color())
        andy.circle(100, steps=100)
        andy.left(gap_size)  
        # could also write instead of andy.left(gap_size):
        # andy.setheading(andy.heading() + gap_size) 
        
if __name__ == '__main__':    
    main()      