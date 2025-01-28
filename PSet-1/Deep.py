#Yes if its either 42 or forty two or forty- two, otherwise No
x=input()
match x:
    case "42"|"forty two"|"forty-two":
        print("Yes")
    case _:
        print("No")
