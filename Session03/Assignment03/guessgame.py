from random import *

num = int(input('''Guess your number game
Now think of a number from 1 to 100, then press Enter '''))
instruction = input('''All you have to do is answer to my guess
'c' if my guess is correct
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number''')

low = 1
high = 100
trial = 0
comp = (low+high)//2
s = comp < num
l = comp > num
c = comp == num

response = "  "
print("Is it", comp, "?")   
response = input()

if response == "s":
    large = (comp + high)//2
    print("Is it", large, "?")
    response = input()
elif response == "l":
    small = (comp + low)//2
    print("Is it", small, "?")  
    reponse = input()
elif response == "c":
    print("I knew it!")

while True:
    for i in range (1,50):
        if response == "s":
            larger = int(large + i)
            guess = randint(larger, 100)
            print(guess)
        elif response == "l":
            smaller = int(small - i)
            guess = randint(1, smaller)
            print(guess)
        elif response == "c":
            print("I knew it!")
            break






