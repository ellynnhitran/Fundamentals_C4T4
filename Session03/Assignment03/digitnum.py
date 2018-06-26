count = 0
number = int(input("Enter a number: "))

while (number > 0):
    number = number // 10
    count += 1

print("it", "has", count, "digit(s)" )

