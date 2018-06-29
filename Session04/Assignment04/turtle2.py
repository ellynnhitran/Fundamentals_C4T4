from turtle import *
shape("turtle")
color("blue")
speed(-1)

for i in range(60):
    for _ in range (4):
        forward(2*i)
        right(90)
    left(10)

mainloop()