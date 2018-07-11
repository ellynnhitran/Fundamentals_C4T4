from turtle import *
shape("turtle")
speed(-1)

for i in range(4,10):
    for j in range (i):
        forward(100)
        left(360//i)
        if j%2 == 0:
            color('blue')
        else:
            color('red')

mainloop()
