num = int(input("Enter a number: "))
result = 0
for i in range (1, num):
    if (num%i)==0:
        result = result + i
if result == num:
    print(num, "is a perfect number!")
else:
    print(num, "is NOT a perfect number")
