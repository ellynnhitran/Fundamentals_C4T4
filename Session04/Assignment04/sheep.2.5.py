size=[5, 7, 300, 90, 24, 50, 75]

for i in range(1,4):
        print("MONTH {0}".format(i))
        size = [50+x for x in size]
        print("One month has passed, now here is my flock",size)
        print("Now my biggest sheep has size ", max(size), "let's shear it")
        newindex = size.index(max(size))
        size[newindex] = 8
        print("After shearing, here is my flock", size, sep=", ")
    








