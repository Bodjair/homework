import random
total_score = 0
num1 = random.randint(1, 5)
num2 = random.randint(1, 5)
for i in range(1, 10):
    result = num1 + num2
    choice = int(input("Enter number: "))
    if result == choice:
        total_score = total_score + 1
        print("You win -", total_score)
print(total_score, "- Total scores.", "\nComputer select number -", result)