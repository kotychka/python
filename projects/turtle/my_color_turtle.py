import turtle

t = turtle.Turtle()
t.speed(0)

def form(lenght, angle):
	for i in range(4):
		t.forward(lenght)
		t.right(angle)

for i in range(360):
	form(100,90)
	t.right(7)




turtle.done()