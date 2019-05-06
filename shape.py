import turtle
from turtle import *

wn = turtle.Screen()
wn.bgcolor('yellow')

t = turtle.Turtle()
t.begin_fill()
t.fillcolor('green')

for i in range(4):
	t.fd(200) # distance 
	t.left(90) # angle

t.end_fill()
t.hideturtle()


wn.mainloop()