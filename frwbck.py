import turtle 
from turtle import *

# set heading like quardinates
wn = turtle.Screen()
wn.title('forword , backword, left  and right')


t = turtle.Turtle()

# forword
t.setheading(70)
t.fd(150)

# backword
t.setheading(250)
t.bk(120)

#left
t.fd(450)
t.left(120) # pass the angle

#right
t.bk(230)
t.right(203)


wn.bgcolor('blue')
wn.mainloop()



