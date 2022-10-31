some_text = input("Enter some text:")
count = len(some_text)
first_pos = int(input("Enter first position: "))
first_pos1 = first_pos - 1
second_pos = int(input("Enter second position: "))
count = str(some_text)
count = some_text[first_pos1:second_pos]
print(count)
