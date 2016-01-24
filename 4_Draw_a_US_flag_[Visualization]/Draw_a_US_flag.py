print ("************" * 1)
print ("Draw A US flag")
print ("************\n" * 1)

import math
import turtle
import tkinter

#### Define function ###
def draw_rectangle(height,length,color):
    # color is input as a string, ex. "violet" "red" or their 8-bit hex, #
    # like "#EE82EE" "#FF0000" #
    turtle.colormode(255)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.setheading(-90)
    for i in range(1,3):
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
    turtle.end_fill()

def draw_star(length,color):
    turtle.goto( turtle.pos() + (0,3.08))
    turtle.colormode(255)
    turtle.fillcolor(color)
    turtle.begin_fill()    
    turtle.setheading(-90)
    turtle.right(18)
    for i in range(1,6):
        turtle.forward(length)
        turtle.right(72)
        turtle.forward(length)
        turtle.left(144)
    turtle.end_fill()

def draw_row(x, y, distance, count):
    for i in range(1,count+1):
        turtle.penup()
        turtle.setpos(x, y)
        draw_star(2.23775, "white")
        x = x + distance
#### Function Definition Finished###

#### Flag Specification ###
H = 6.33
F = 5.38
L = 6.16



x = H
y = 100
count = 0

# Draw two rectangle #
turtle.goto(0,100)
draw_rectangle(100,190,"white")

turtle.goto(0,100)
draw_rectangle(7.69,190,"#B22234")

# Draw strips #
while turtle.ycor() > 17:
    turtle.penup()
    turtle.goto( turtle.pos() + (0,-15.385))
    draw_rectangle(7.69,190,"#B22234")

turtle.penup()
turtle.goto(0,100)
draw_rectangle(53.85,76,"#3C3B6E")

# Draw stars #
for i in range(1,10):
    y = y - F
    if i % 2 == 0:
        count = 5
        x = x + H
        draw_row(x,y,6.33*2,count)
    else:
        count = 6
        x = H
        draw_row(x,y,6.33*2,count)

# Output Image as .eps #
ts = turtle.getscreen()
ts.getcanvas().postscript(file="flag.eps")

turtle.setpos(0,0)
turtle.mainloop()


