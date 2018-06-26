from turtle import *
shape("turtle")
speed(-1)

for i in range (3,8):
    for k in range (i):
        if i == 3:
            color("red")
        elif i == 4:
            color("blue")
        elif i == 5:
            color("purple")
        elif i == 6:
            color("yellow")
        elif i == 7:
            color("grey")
        forward(100)
        left(360//i)

mainloop()






# t = turtle.Turtle()
# pen_color=("red", "blue", "purple", "yellow", "grey")