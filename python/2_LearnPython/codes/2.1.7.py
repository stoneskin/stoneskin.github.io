import turtle

t= turtle.Pen()

colors = ['red','yellow','blue','green']

for x in range(0,100): # repeat 100 times
    # Draw line with length 100
    t.forward(10*x)

    # make turn 90 degree and draw another line
    t.left(90)
    t.pencolor(colors[x%4])
    
