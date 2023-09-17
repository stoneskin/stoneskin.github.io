import turtle

t= turtle.Pen()

colors = ['red','yellow','blue','green']

n= int( turtle.numinput("Input", "Give the number of loops you need run.", default=10, minval=10, maxval=100))

for x in range(0,n): # repeat 100 times
    # Draw line with length 100
    t.forward(10*x)

    # make turn 90 degree and draw another line
    t.left(90)
    t.pencolor(colors[x%4])
    

ok= turtle.textinput("ok!","Click OK to Exit.")
print(ok)
turtle.bye()
##when you click the screen, exit the python
#turtle.exitonclick()