
def get_even_list(l):
    # list = (l)
    even_list = []
    # even=[]
    for item in l:
        if item%2 == 0:
            even_list.append(item)
    # even_list=[ ]
    # even_list.append(even)
    print(*even_list, sep=",")
    return even_list


get_even_list([1, 4, 5, -1, 10])
