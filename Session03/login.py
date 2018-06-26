import getpass

print ("Hi there, this is a superuser gateway")
user = input("Username: ")
print (user)

if user == "c4t":
    password = getpass.getpass("Password: ")
    if password == "codethechange":
        print("Welcome, c4t")
    else:
        print("Password is incorrect")
elif user != "c4t":
    print("You are not superuser")