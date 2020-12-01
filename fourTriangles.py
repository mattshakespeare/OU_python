#draw four triangles
#from turtle import*

number_of_shapes = 4

for shapes in range(number_of_shapes):
    for triangle in range(3):
        forward(50 + shapes * 10)
        left(120)
    penup()
    forward(30 + shapes * 10)
    pendown()
