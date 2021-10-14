import turtle,random
border=turtle.Turtle()
border.shape('circle')
border.speed(0)
border.color("pink")
border.width(5)
border.hideturtle()
border.penup()
border.goto(250,0)
border.down()
border.goto(250,250)
border.goto(-250,250)
border.goto(-250,-250)
border.goto(250,-250)
border.goto(250,0)

ball = turtle.Turtle()
ball.shape("circle")
dx=random.randint(1,5)
dy=random.randint(1,5)
rstart=random.randint(-250,250)
x=0
y=0
ball.penup()
ball.goto(x + rstart, y + rstart)
while True:
    x,y = ball.position()
    ball.penup()
    if x+dx > 250 or x+dx < -250:
        dx = -dx
    if y+dy > 250 or y+dy < -250:
        dy = -dy

    ball.goto(x+dx,y+dy)

