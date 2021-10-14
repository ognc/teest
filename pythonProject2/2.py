import turtle
turtle.width(3)
A1 = [-45, 50*2**(1/2), -225, 100]   # нечетные поворот, четные движение
A4 = [0, 50, -90, 50, -90, 50, 180, 100]
A7 = [-90, 50, 135, 50*2**(1/2), -45, 50]
A0 = [-90, 50, 90, 100, 90, 50, 90, 100]

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
for i in range(0, len(A1)):
    if (i+1) % 2 != 0:
        turtle.right(int(A1[i]))
    else:
        turtle.forward(int(A1[i]))

turtle.penup()
turtle.goto(110, 0) #расстояние - 40
turtle.pendown()
for i in range(0, len(A4)):
    if (i+1) % 2 != 0:
        turtle.right(int(A4[i]))
    else:
        turtle.forward(int(A4[i]))

turtle.penup()
turtle.goto(220, -50)
turtle.pendown()
turtle.left(90)
for i in range(0, len(A1)):
    if (i+1) % 2 != 0:
        turtle.right(int(A1[i]))
    else:
        turtle.forward(int(A1[i]))

turtle.penup()
turtle.goto(330, 0)
turtle.pendown()
for i in range(0, len(A7)):
    if (i+1) % 2 != 0:
        turtle.right(int(A7[i]))
    else:
        turtle.forward(int(A7[i]))

turtle.penup()
turtle.goto(440, 0)
turtle.pendown()
for i in range(0, len(A0)):
    if (i+1) % 2 != 0:
        turtle.right(int(A0[i]))
    else:
        turtle.forward(int(A0[i]))

turtle.penup()
turtle.goto(550, 0)
turtle.pendown()
turtle.left(-180)
for i in range(0, len(A0)):
    if (i+1) % 2 != 0:
        turtle.right(int(A0[i]))
    else:
        turtle.forward(int(A0[i]))
