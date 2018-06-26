num = int(input("Enter a number: "))

while True:
    if num > 1:
        for i in range (2,num):
            if num%i == 0:
                print("It isn't a prime number.")
                break
            else:
                print("It is a prime number.")
                break
    else: 
        print ("It is a prime number.")
        break