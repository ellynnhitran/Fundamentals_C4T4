from turtle import *
import random

speed(-1)
shape("turtle")

colors = ["black", "grey"]
color = random.choice(colors)

for i in range(1,120):
    forward(i*3)
    left(90)

mainloop()
