import sys

colours = ["Black", "Orange", "Blue", "Green", "Yellow", "Pink", "Magenta", "Grey", "White", "Purple"]
first_index = int(input("Enter first index from zero to four: "))
if first_index < 0 or first_index > 4:
    print("incorrect number")
    sys.exit()
end_index = int(input("Enter end of index from five to nine: "))
if end_index < 5 or end_index > 9:
    print("incorrect number")
    sys.exit()
result_colours = []
for i in range(first_index, end_index + 1):
    result_colours.append(colours[i])
print(result_colours)