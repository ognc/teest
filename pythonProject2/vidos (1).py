import turtle as t
t.shape("circle")
Vy=7
Vx=1.5
ay=-0.1
time=2
while True:
    Vy=Vy+ay*time
    t.goto(t.xcor()+Vx*time,t.ycor()+Vy*time + (ay*time**2)/2)


    time +=0.002
    if t.ycor()<=0:
        Vy=-Vy
        Vy=Vy+ay*time
    if t.ycor()<-88.9:
        break


