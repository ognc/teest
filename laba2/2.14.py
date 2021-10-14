#2.14
import turtle
turtle.speed(4)
def star(n):
    for i in range(0,n):
        turtle.forward(180)
        turtle.left(180-(180/n))
star(int(input()))
