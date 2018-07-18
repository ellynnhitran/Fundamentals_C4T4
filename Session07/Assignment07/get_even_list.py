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

get_even_list([1, 4, 5, -1, 10])
