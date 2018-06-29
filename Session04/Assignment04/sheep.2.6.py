size=[5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hiep and there are my ship sizes", size)
print("Now my biggest sheep has size ", max(size), "let's shear it")
index = size.index(max(size))
size[index] = 8
print("After shearing, here is my flock", size, sep=", ")

for i in range(1,4):
    if i < 3:
        print("MONTH {0}".format(i))
        size = [50+x for x in size]
        print("One month has passed, now here is my flock",size)
        print("Now my biggest sheep has size ", max(size), "let's shear it")
        newindex = size.index(max(size))
        size[newindex] = 8
        print("After shearing, here is my flock", size, sep=", ")
    elif i == 3:
        print("MONTH {0}".format(i))
        size = [50+x for x in size]
        print("One month has passed, now here is my flock",size)    
        
        
sum = sum(size)
print("My flock has size in total: ", sum)
print("I would get {0} * 2$ = 2020$".format(sum))








