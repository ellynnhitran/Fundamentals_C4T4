from turtle import *

shape("turtle")
speed(-1)

for i in range(4):
    for _ in range (4):
        forward(100 + i*10)
        left(90)
    right(60)

# for i in range(4):
#     forward(50)
#     left(90)


# right(60)
# for i in range(4):
#         forward(150)
#         left(90)

# right(60)
# for i in range(4):
#         forward(200)
#         left(90)

# right(60)
# for i in range(4):
#         forward(250)
#         left(90)

mainloop()

