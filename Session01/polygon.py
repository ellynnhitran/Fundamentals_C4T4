from turtle import *
speed(-1)
shape("turtle")
color("purple")

# number = int(input("How many polygons you need?"))
# ans = 0 + int(number)
# print("I want", ans)

n = 5

for i in range(n): 
    forward (100)
    left(360//n)
    

mainloop()