numbers = [-1,-20,0,-10]
sorted_list=[ ]

while True:
    if len(numbers) != 0:
        sorted_list.append(min(numbers))
        numbers.remove(min(numbers))
    else:
        print(*sorted_list,sep=", ")
        break
    