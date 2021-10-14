import turtle as t, random
Vy=1
Vx=1
a=-0.02
T=0
x=0
y=0
while True:
    if y>=0:
        t.goto(x,y)
        x +=x+Vx*T*a
        y +=y+Vy*T*a - a*T**2/2
        Vy += a*T
        T+=0.2
    else:
        Vy = -Vy


