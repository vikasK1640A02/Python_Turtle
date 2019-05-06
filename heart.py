import turtle
from turtle import *

wn = turtle.Screen()
wn.bgcolor('green')


t=turtle.Turtle()
t.begin_fill()
t.fillcolor('red')
t.setheading(140)
t.fd(180)
t.circle(-90,200)

t.setheading(60)
t.circle(-90,200)
t.fd(180)
t.end_fill()
t.hideturtle()


wn.mainloop()