import random
runnum = random.randint(1, 10)
choice = int(input("Select number from 1 to 10: "))
while choice != runnum:
    print("Wrong choice")
    if choice < runnum:
        print("Too lo")
    else:
        print("too high")
    choice = int(input("One more time: "))
print("You WIN! Computer select -", runnum)