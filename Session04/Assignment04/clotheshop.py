items = ["T-shirt", "Sweater"]

while True: 
    response = input("Welcome to our shop, what do you want (C, R, U, D)? ")

    if response == "R":
        print("Our items:", *items)
    elif response == "C":
        add = input("Enter new item: ")
        items.append(add)
        print("Our items:", *items)
    elif response == "U":
        update = int(input("Update position? "))
        replace = input("New items? ")
        items[update-1] = replace
        print("Our items:", *items)
    elif response == "D":
        delete = int(input("Delete position? "))
        del items[delete-1]
        print("Our items:", *items)

