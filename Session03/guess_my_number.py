from random import randint
numb = randint(1,100)
count = 0
playing = True

while playing:
    guess = int(input("Guess my number: "))
    print(guess)
    
    if guess > numb:
        print("Too large")
    elif guess < numb:
        print("Too small")
    elif guess == numb:
        print("Bingo")
        break 

    count += 1
    if count == 7:
        print("You lose")
        break
    
   