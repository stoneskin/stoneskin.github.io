import turtle,time

shape_list=["blank","arrow","circle","classic","square","triangle","turtle"]

for shape_number in range(7):
    shapename=shape_list[shape_number]
    t= turtle.Pen()
    t.stamp()  
    t.shape(shapename)
    t.forward(10+shape_number*20)
    t.left(90)
    t.forward(10+shape_number*20)
  
    time.sleep(1)
    


time.sleep(10)