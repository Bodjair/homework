again = "y"
summa = 0
while again == "y":
    number = int(input("Enter number: "))
    again = input("Enter new number? press (y) or (n)")
    summa = summa + number
    print("Summa is:", summa)