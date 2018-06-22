from turtle import *

shape("turtle")
speed(-1)

color("red")
for i in range(4):
        forward(100)
        left(90)

color("blue")
n=3
for i in range (n):
    forward(100)
    left(360//n)

color("blue")
n2=5
for i in range(n2):
    forward(100)
    left(360//n2)

color("red")
n3=6
for i in range(n3):
    forward(100)
    left(360//n3)

mainloop()
