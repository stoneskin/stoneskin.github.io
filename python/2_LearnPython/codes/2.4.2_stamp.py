import turtle,time

turtle.bgcolor("blue")
t = turtle.Turtle() # same as turtle.Pen()

t.shape("turtle")
t.color("lightgreen")

t.penup()
size=15
for i in range(30):
    t.stamp()
    size=size+2
    t.forward(size)
    t.right(30)

time.sleep(10)