import turtle
wn=turtle.Screen().bgcolor("white")
t=turtle.Turtle()
t.goto(0,200)
a=0
b=0
t.speed(10)
t.pencolor("blue")
while True:
    t.forward(a)
    t.right(b)
    a=a+3
    b=b+1
    if b==210:
        break
    t.hideturtle()

