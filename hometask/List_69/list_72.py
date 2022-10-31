predmety = ["Math", "Geography", "Biology", "Physics"]

while True:
    unlike_predmet = input("Enter ulike predmet:")
    if unlike_predmet == "exit":
        break
    if unlike_predmet in predmety:
        predmety.remove(unlike_predmet)
        print(predmety)
    else:
        print(f"no {unlike_predmet} in {predmety}")
