from random import choice
words = ["champion", "humanity", "atmosphere"]
word = choice(words)
chars = list(word)

while len(chars) > 0:
    rand_char = choice(chars)
    print(rand_char, end = " ")    
    chars.remove(rand_char)
    if len(chars) == 0:
        break
print()
while True:
    ans = input("Your guess: ")
    if ans == word:
        print("Hura")
        break
    else:
        print(":<")