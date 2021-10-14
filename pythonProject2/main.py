from random import randint
import turtle
cherep = 9
kol = 500
turtle.speed(500)
turtle.penup()
turtle.goto(220,220)
turtle.pendown()
turtle.backward(440)
turtle.left(90)
turtle.backward(440)
turtle.left(90)
turtle.backward(440)
turtle.left(90)
turtle.backward(440)
turtle.left(90)

g = [turtle.Turtle(shape='arrow') for i in range(cherep)]
for unit in g:
    unit.penup()
    unit.speed(500)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.left(randint(-360, 360))

for i in range(kol):
    for unit in g:
        if unit.xcor() > 200:
            if unit.towards(200, 200) > 90:
                print(unit.towards(200, -200))
                unit.left(90)
                unit.goto(200,unit.ycor())
            else:
                unit.right(180)
        unit.forward(7)
