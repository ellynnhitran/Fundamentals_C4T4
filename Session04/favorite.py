print("Hi there, here you favorite things so far")
favorite = ["death note","netflix","teaching"]
print(*favorite, sep=", ")
# add = input("Name one thing you want to add? ")
# favorite.append(add)
# print(*favorite, sep=", ")

print("* " *30)

for index, item in enumerate(favorite):
    print(index+1, item, sep=".")
print("* " *30 )

position = int(input("Position you want to update? "))
replace = input("Your replacing favorite? ")
favorite[position-1] = replace

print("* " *30)
for index, item in enumerate(favorite):
    print(index+1, item, sep=".")
print("* " *30 )
    



