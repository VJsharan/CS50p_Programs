# takes the given i/p as string and does the operation specified,it splits the string into elements based on their whitespaces among them
# and then performed the operation, and  gives the result as a float, eg : if its 2 * 5 -> 10.0
given=input("Expression : ").split()
y=int(given[-1])
x=int(given[0])
match (given[1]):
    case '+':
        print(float(x+y))
    case '-':
        print(float(x-y))
    case '*':
        print(float(x*y))
    case '/':
        print(float(x/y))

