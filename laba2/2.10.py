#2.10
import turtle
n = int(input())
turtle.speed(4)
def circle(s):
    turtle.circle(s)
for i in range(0, n):
    turtle.left(360 / n)
    circle(90)
    circle(-90)

