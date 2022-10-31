person = int(input("Enter number of persons: "))
if person < 10:
    for _ in range(0, person):
        name = input("Enter name: ")
        print(name, "has ben invited")
else:
    print("too many people")