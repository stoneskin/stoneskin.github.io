# Code sample MyFirstTurtle.py
import turtle,time

t = turtle.Pen()
t2 = turtle.Pen()

# Draw line with length 100
t.forward(100)
t2.forward(100)

# make turn 90 degree and draw another line
t.left(90)
t.forward(100)
t2.right(90)
t2.forward(100)

# continue turn and drawing line twice
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

t2.right(90)
t2.forward(100)
t2.right(90)
t2.forward(100)

# waiting 10 sec and exit python running window
#time.sleep(10)

#turtle.exitonclick()

turtle.textinput("ok!","Click OK to Exit.")



