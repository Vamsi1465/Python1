import turtle
screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(2)
colors = ['red', 'orange', 'yellow','green', 'blue', 'indigo', 'violet']
for color in colors:
    pen.color(color)
    pen.forward(100)
    pen.left(90)
