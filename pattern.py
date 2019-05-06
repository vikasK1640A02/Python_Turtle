import turtle

wn = turtle.Screen()
wn.bgcolor('pink')

t=turtle.Turtle()
list1=['red','green','blue','orange','purple']
for i in range(100):
	t.speed(0)
	t.color(list1[i%5])
	t.pensize(i/10+1)
	t.fd(i)
	t.left(59)

wn.mainloop()