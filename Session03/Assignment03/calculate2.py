num = int(input("Enter a number: "))
S = 0
for i in range (1,num+1):
    fac = i*i
    S = S + 1/fac

print(S)