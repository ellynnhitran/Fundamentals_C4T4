from turtle import *
shape("turtle")
speed(-1)
color("blue")

for _ in range(40):
    for _ in range(4):
        forward(200)
        right(90)
    right(10)

mainloop()