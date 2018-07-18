from turtle import *
speed(-1)
def draw_square(length1,color1):
    color(color1)
    for i in range (4):
        forward(length1)
        left(90)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()