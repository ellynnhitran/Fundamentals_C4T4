from turtle import *

shape("turtle")
speed(-1)
color("blue")

for i in range(50):
    for _ in range (4):
        forward(i*10)
        left(90)
    left(10)
    forward(10)

mainloop()