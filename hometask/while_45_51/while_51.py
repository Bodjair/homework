bottles = 5
while bottles < 0:
    print(f"{bottles} green bottles hanging on the wall, and if 1 green bottle should accidentally fall")
    num = int(input(f"how many green {bottles} will be hanging on the wall?"))
    bottles = bottles - num
    print(bottles)

# NOT COMLETED