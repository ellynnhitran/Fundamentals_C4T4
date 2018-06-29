from turtle import *
shape("turtle")
speed(-1)


# for i in range(4):
#     forward(100)
#     left(90)

# for i in range(2):
#     right(60)
#     for i in range(4):
#         forward(100)
#         left(90)

for i in range(3):
    for _ in range (4):
        forward(100)
        left(90)
    right(60)

mainloop()