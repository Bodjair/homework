compnum = 50
count = 0
num = int(input("Guess, and enter number: "))
while num != compnum:
    if num < compnum:
        print("too lo")
    else:
        print("To high")
    num = int(input("Enter another number? "))
print("Well done")