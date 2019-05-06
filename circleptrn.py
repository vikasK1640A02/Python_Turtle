import turtle
from turtle import *
wn = turtle.Screen()
wn.bgcolor('yellow')

t=turtle.Turtle()
list1=['red','green','blue','orange']
t.up()
t.goto(0,100)

for i in range(4):
	t.down()
	t.begin_fill()
	t.fillcolor(list1[i])
	t.circle(50)
	t.end_fill()
	t.up()
	t.bk(100)
	


wn.mainloop()