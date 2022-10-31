num = int(input("Enter number from 10 to 20: "))
while num < 10 or num > 20:
    if num < 10:
        print("to low")
    elif num > 20:
        print("To high")
    num = int(input("Enter another number: "))
print("Thank you!")