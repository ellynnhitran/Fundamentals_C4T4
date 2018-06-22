from turtle import *

speed(-1)
shape("turtle")
color ("green")

begin_fill()

n = 3
for i in range (n):
    forward(100)
    left(360//n)

color("yellow")
end_fill()

mainloop()