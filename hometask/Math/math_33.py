number = int(input("1) Square \n2) Triangle\n Enter a number: "))
if number == 1:
    sqare = int(input("Enter side leight of the sqare: "))
    sqare_res = sqare ** 2
    print("Ploshcha kvadrata = ",sqare_res)
elif number == 2:
    num_l = int(input("Enter side leight of the treangle: "))
    num_h = int(input("Enter side high of the treangle: "))
    treagl = num_h * num_l
    print("Ploshaca triangle = ",treagl)
else:
    print("ERROR!")
