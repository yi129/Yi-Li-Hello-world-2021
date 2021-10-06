import turtle 
painter = turtle.Turtle()
s = turtle.Screen()
painter.speed(0)
c = 0
d = 0
s.bgcolor("black")
painter.pencolor("gray")
while True:
    for i in range(4):
        painter.forward(60)
        painter.right(90)
    painter.right(15)
    c += 1 
    if c >= 390/15:
        painter.forward(60) 
        c = 0
        d += 1 
        if d >= 12:
            break 

turtle.done()