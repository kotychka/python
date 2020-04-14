import turtle
win = turtle.Screen()
win.bgcolor('green')
tort = turtle.Turtle()
tort.color('blue')
tort.shape('turtle')
tort.up()
for size in range(5, 200, 2):
    tort.stamp()
    tort.forward(size)
    tort.right(50)
turtle.done()