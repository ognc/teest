# 2.9
import turtle
turtle.speed(4)
turtle.shape('turtle')
n = 3
f = 0
x = 0
y = 0
for i in range(0, 10):
    for j in range(0, n):
        turtle.forward(50 + f)
        turtle.left(360/n)
    turtle.up()
    n = n + 1
    f = f + 5
    x = x - 3
    y = y - 2 * n
    turtle.pos()
    turtle.setpos(x,y)
    turtle.down()
