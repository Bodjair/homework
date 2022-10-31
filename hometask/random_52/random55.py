import random
runnum = random.randint(1, 5)
choice = int(input("Select number from 1 to 5: "))
if choice == runnum:
    print("Well done")
elif choice > runnum:
    print("too high")
    choice = int(input("Second choice: "))
    if choice == runnum:
        print("You win")
    else:
        print("You lose")
elif choice < runnum:
    print("to low")
    choice = int(input("Second choice: "))
    if choice == runnum:
        print("You win")
    else:
        print("You lose")
else:
    print("BAD LUCK")
print("Computer select -", runnum)