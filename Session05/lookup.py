dictionary= {
    "hc": "hoc",
    "ng": "nguoi",
    "pt": "phat trien",
    "eny": "em nguoi yeu",
    "any": "anh nguoi yeu",
    "ns": "noi",
    "ngta": "nguoi ta",
    "lm": "lam",
    "r": "roi",
    "stt": "status"
}
while True:
    for key in dictionary.keys():
        print(key, end="\t")
    print() 

    code = input("Your code: ")
    
    if code in dictionary:
        print("Translation: ", dictionary[code])
    else:
        print("Not found")
        contribute = input("Do you want to contribute this word (Y/N)?".lower())
        if contribute == "y":
            trans = input("Enter your translation: ")
            dictionary[code] = trans
        elif contribute == "n":
            print("Bye")
            break
            
