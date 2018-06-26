num = int(input('''Guess your number game
Now think of a number from 1 to 100, then press Enter '''))
instruction = input('''All you have to do is answer to my guess
'c' if my guess is correct
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number''')

low = 0
high = 100
trial = 0
comp = (low+high)//2
s = comp < num
l = comp > num
c = comp == num

response = "  "
print("Is it", comp, "?")   
response = input()

while True:
    trial += 1
    if response == "s":
        low = comp
        comp = (low + high)//2
        print("Is it", comp, "?")
        response = input()
    elif response == "l":
        high = comp
        comp = (high + low)//2
        print("Is it", comp, "?")  
        reponse = input()
    elif response == "c":
        print("I knew it!")
        break

