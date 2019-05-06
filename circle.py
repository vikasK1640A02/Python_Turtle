import turtle
from turtle import *

wn = turtle.Screen()
wn.bgcolor('red')
wn.title('circle with goto')

t1=turtle.Turtle()
#t2=turtle.Turtle()
#t3=turtle.Turtle()

t1.up()
t1.goto(-50,50) # move the position of circle

t1.begin_fill()
t1.fillcolor('green')

t1.down()
t1.circle(100, steps=6) #100 is radius for hexagon

t1.end_fill()
t1.hideturtle()

#t2.circle(100, extend=120) # 120 is angle
#t3.circle(100, ) # 100 is radius



wn.mainloop()