import turtle,time

t=turtle.Pen()

number_of_shapes = 4

t.penup()
t.goto(-10*3,10*3)
t.fillcolor("green")
t.begin_fill()
t.pendown()
l=10*2*3
t.forward(l)
t.right(90)
t.forward(l)
t.right(90)
t.forward(l)
t.right(90)
t.forward(l)
t.right(90)
t.end_fill()

t.penup()
t.goto(-10*2,10*2)
t.fillcolor("yellow")
t.begin_fill()
t.pendown()
l=10*2*2
t.forward(l)
t.right(90)
t.forward(l)
t.right(90)
t.forward(l)
t.right(90)
t.forward(l)
t.right(90)
t.end_fill()

t.penup()
t.goto(-10,10)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
l=10*2*1
t.forward(l)
t.right(90)
t.forward(l)
t.right(90)
t.forward(l)
t.right(90)
t.forward(l)
t.right(90)
t.end_fill()

t.hideturtle()


    
time.sleep(10)
