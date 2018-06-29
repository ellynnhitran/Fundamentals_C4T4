size=[5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hiep and there are my ship sizes", size)
print("Now my biggest sheep has size ", max(size), "let's shear it")
index = size.index(max(size))
size[index] = 8
print("After shearing, here is my flock", size, sep=", ")