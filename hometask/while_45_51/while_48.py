count = 0
again = "y"
while again == "y":
    name = input("Enter name for inviting: ")
    print(name, "- has been invited")
    again = input("Enter another name? (y) or (n) \n")
    count = count + 1
    print(count, "- Total persons invited")