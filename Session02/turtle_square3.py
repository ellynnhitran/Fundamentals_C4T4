from turtle import *

shape("turtle")
speed(-1)
color("grey")

for i in range(60):
    for _ in range (4):
        forward(i*8)
        left(90)
    left(10)
    forward(10)

mainloop()