import turtle,time

#example of draw a Micky mouse

t = turtle.Pen()
t.circle(100)  # draw the center circle

t.penup()
t.goto(100,100) 
t.pendown()
t.circle(70)

t.penup()
t.goto(-100,100)
t.pendown()
t.circle(70)

time.sleep(10)
