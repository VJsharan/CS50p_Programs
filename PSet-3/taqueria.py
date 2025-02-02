'''
# Problem : To enter the foods, and once CTRL + D is pressed, it has to display the total amount
# Solution : 
    • val is initialized to 0.00 for float purposes and the dict is initialized too.
    • Then the inputs are obtained and converted into TitleCase since it’s like that in the dict.
    • Then, if the input is either empty ' ' or not in given, it’s redone.
    • Otherwise, if the input is there in the given dict, the value of that key is taken and incremented to the bill amount.
    • This process is done repeatedly until CTRL + D is pressed.
    • If a KeyError is caught, it’s redone.
    • Once CTRL + D is pressed, the program is exited using sys.exit().
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

