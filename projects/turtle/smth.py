import turtle
win = turtle.Screen()
win.bgcolor('black')
color = ['red', 'blue', 'yellow', 'green', 'lightblue', 'orange','lightgreen']
tort = turtle.Turtle()
for itr in range(360):
    tort.color(color[itr%7])
    tort.forward(itr)
    tort.left(62)
turtle.done()