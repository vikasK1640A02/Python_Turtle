def draw_circle(x,y,color,rad):
	t.up()
	t.goto(x,y)
	t.begin_fill()
	t.fillcolor(color)
	t.down()
	t.circle(rad)
	t.end_fill()
	t.up()
	t.home()



import turtle
from turtle import *

wn = turtle.Screen()
wn.bgcolor('green')

# set the turtle
t = turtle.Turtle()
draw_circle(0,0,'black',50)
draw_circle(150,-150,'red',50)
draw_circle(150,150,'yellow',50)
draw_circle(-150,150,'blue',50)
draw_circle(-150,-150,'orange',50)

wn.mainloop()