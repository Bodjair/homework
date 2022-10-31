word = input("Enter word: ")
first_s = word[0]
if first_s == "a" or first_s == "o" or first_s == "i" or first_s == "u":
    result = word + first_s + "oy"
    print(result[1:].lower())
else:
    print(word + "way".lower())