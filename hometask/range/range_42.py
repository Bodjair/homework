total = 0

for _ in range(5):
    x = int(input("Enter number: "))
    answer = input("Add number to total (y/n)?: ")
    if answer == "y":
        total = total + x
    print(total)