#from turtle import *
def draw_triangle(side_length):
    '''Draws a triangle'''
    pendown()
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)
    penup()

draw_triangle()
forward(300)
draw_triangle()
left(120)
forward(300)
draw_triangle()
