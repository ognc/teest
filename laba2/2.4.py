#2.6
import turtle

turtle.shape('arrow')
n = int(input())
for i in range (0,n):
    turtle.forward(160)
    turtle.end_fill()
    turtle.stamp()
    turtle.goto(0, 0)
    turtle.right(360/n)
