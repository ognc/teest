#2.11
import turtle
turtle.speed(4)
turtle.left(90)
f = 0
def circle(n):
    turtle.circle(n)
while 1 != 0:
    circle(50 + f)
    circle(-50 - f)
    f = f + 10
