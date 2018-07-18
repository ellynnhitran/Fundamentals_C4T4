from random import choice, randint
import eval
x = randint(1,11)
y = randint(1,11)
op1 = ["+", "-", "*", "/"]
op = choice(op1)

res = eval.calc(x, y, op)

error = choice([-1,0,0,1])
display = res + error
print(x, op, y, "=", display)
ans = input("(Y/N)? ").lower()

if ans == "y":
    if error == 0:
        print("Yay")
    else:
        print("You are wrong :<")
elif ans == "n":
    if error == 0:
        print("You are wrong :<")
    else:
        print("Yay")








