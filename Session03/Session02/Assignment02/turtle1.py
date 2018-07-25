from turtle import *

shape("turtle")
color("red")
speed(-1)

left(30)

for i in range (4):
    for k in range (2):
        forward(100)
        right (60)
        forward(100)
        right(120)

    left(90)
    
mainloop()
