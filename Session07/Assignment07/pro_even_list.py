def get_even_list(l):
    list = (l)
    even=[]
    for item in list:
        if item%2 == 0:
            even.append(item)

    sorted_list=[ ]
    sorted_list.append(even)

    print(*sorted_list)
    return sorted_list

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
