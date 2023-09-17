# Drawing 100 squares
import turtle
t= turtle.Pen()

turtle.speed(9)

for x in range(0,100): # repeat 100 times
    # Draw line with length 100
    t.forward(100+x)

    # make turn 90 degree and draw another line
    t.left(90)
    t.forward(100+x)

    # continue turn and drawing line twice
    t.left(90)
    t.forward(100+x)
    t.left(90)
    t.forward(100+x)
    print(x) # x will be from 0 to 99
    
input("Enter any to exit\n")