city_list = ("Kiev", "Varshava", "London", "Riga", "Praha",)
print(city_list)
city_input = input("Enter name one of the city: ")
print(city_input, "Has index: ", city_list.index(city_input))
num = int(input("Enter number from 0 to 4:" ))
print(city_list[num])
