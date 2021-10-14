#2.5
import turtle
turtle.shape('turtle')
n1 = 100
y = float(1)
x = float(1)
for i in range(0,10):
    turtle.forward(n1)
    turtle.left(90)
    turtle.forward(n1)
    turtle.left(90)
    turtle.forward(n1)
    turtle.left(90)
    turtle.forward(n1)
    turtle.left(90)
    turtle.forward(n1)
    n1 = n1 + 40
    turtle.penup()
    x = x - 21
    y = y - 21
    turtle.goto(x,y)
    turtle.pendown()
