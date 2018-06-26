from turtle import *
speed(-1)
shape("turtle")

for i in range(1,120):
    forward(i*3)
    left(90)
if i%2 == 0:
    color("grey")
else:
    color("black")


mainloop()
