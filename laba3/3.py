import turtle
turtle.shape("circle")
Vy = 5
Vx = 0.6
ay = -0.1
time = 1
while True:
    Vy = Vy + ay * time
    turtle.goto(turtle.xcor() + Vx * time, turtle.ycor() + Vy * time + (ay * time**2)/2)
    time += 0.02
    if turtle.ycor() <= 0:
        Vy = -Vy
        Vy = Vy + ay * time
    if turtle.ycor() < -10.0:
        break