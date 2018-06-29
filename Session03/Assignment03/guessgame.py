num = int(input('''Guess your number game
Now think of a number from 1 to 100, then press Enter '''))
instruction = input('''All you have to do is answer to my guess
'c' if my guess is correct
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number''')

low = 0
high = 100
mid = (low+high)//2
playing = True
response = input("Is {0} your number: ".format(mid)).lower()
# response = "  "
# print("Is it", mid, "?")   
# response = input()

while playing:
    if response == "s":
        low = mid
        mid = (low + high)//2
        print("Is it", mid, "?")
        response = input()
    elif response == "l":
<<<<<<< HEAD
        high = mid
        mid = (high + low)//2
        print("Is it", mid, "?")  
        response = input()
    elif response == "c":
        print("I knew it!")
        playing = False
    else:
        playing = False

=======
        high = comp
        comp = (high + low)//2
        print("Is it", comp, "?")  
        response = input()
    elif response == "c":
        print("I knew it!")
        break
>>>>>>> b86d15b736eb8cd74588c49b58f41063052a2017

