import turtle,time

#example of draw a Micky mouse

t = turtle.Pen()
angle=144
length=200
t.fillcolor("red")
t.color("red")
t.begin_fill()
for i in range(5):
    t.fd(length)
    t.right(angle)
t.hideturtle()
t.end_fill()
time.sleep(10)