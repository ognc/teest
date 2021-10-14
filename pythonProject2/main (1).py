from random import randint

import turtle
turtle.speed(1)
Vx=1.5
Vy=1.5
t=0
ay=-0.05

y=0
x=0
while True:
    if y >= 0:
        turtle.goto(x,y)
        x += Vx * t
        y += Vy * t + (ay * t ** 2) / 2
        Vy += ay * t
        t+=0.02
    else:
        Vy = -Vy
        x += Vx * t
        y += Vy * t + (ay * t ** 2) / 2
        turtle.goto(x,y)
        t += 0.02