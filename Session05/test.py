# minh_duc = ["Minh Duc", "Son La", 19, 2, 1, 10]

#dictionary/ object/ map

#key: value
#create new 
person = {
    "name": "Duc cop", 
    "age": 19,
    "ex": 2,
    "iq": 1
}
# print(person)
# # add/update new key - value
# person["hometown"] = "Son La"
# print(person)
# person["ex"] = 3
# print(person)

# #read
# print(person["name"])
# for key in person.keys():
#     print(key, end="\t") 


# for key in person.keys():
#     print(person[key])

# for value in person.values():
#     print(value)

key = "age"
if key in person:
    print(person[key])
else:
    print("Not found")
    ask = input("Do you want to contribute to dictionary (Y/N")







