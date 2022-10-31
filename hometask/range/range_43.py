# 43

count = int(input("In wich way will be count? From 1 to hi Enter 1, or from 20 to lo, Enter 2 : "))
if count == 1:
    num_1 = int(input("Enter number: "))
    for _ in range(1, num_1 + 1):
        print(_)
elif count == 2:
    num_1 = int(input("Enter number menshe 20: "))
    for _ in range(20, num_1, -1):
         print(_)
else:
    print("I don`t understand")