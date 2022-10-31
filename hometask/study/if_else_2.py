import sys

num = int(input("Enter eny positive number: "))

if num < 0:
    print("Number must be positve")
    sys.exit()

remainder = num % 2
if remainder == 0:
    print("your number is EVEN")
else:
    print("Your number is ODD")
