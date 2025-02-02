'''#problem : to enter the food, and one CTRL + D is pressed, it has to display the total amount
# Solution : 

'''
import sys
val=0.00
given = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
while True:
    try:
        item = input("Item: ").title()
        if item=='':
            continue
        if item in given:
            val+=float(given[item])
            print(f"\nTotal ${val:.2f}")
    except KeyError:
        pass
    except EOFError:
        sys.exit()

