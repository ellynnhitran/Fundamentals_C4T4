# operations = {+, -, *, /}
x = float(input("x = "))
ask = input("Operations(+,-,*,/): ")
y = float(input("y = "))

if ask == "+" :
    ans = x + y
elif ask == "-" :
    ans = x - y
elif ask == "*" :
    ans = x * y
elif ask == "/":
    ans = x / y

print("* "*10)
print("x", ask, "y", "=", ans) #print("{0} {1} {2} = {3}".format(x, ask, y, =. ans))
print("* "*10)