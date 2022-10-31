name = input("Enter your name: ")
if len(name) < 5:
    family = input("Enter your family: ")
    name = name+family
    print(name.upper())
else:
    print(name.lower())