import turtle,time
from turtle import circle

t= turtle.Pen()

t.fillcolor("violet") #define the color to fill
t.begin_fill()   # start to fill color

t.circle(100)
t.right(90)
t.circle(100)

t.end_fill()  # end to fill color

t.right(90)
t.circle(100)
t.right(90)
t.circle(100)

time.sleep(10)
