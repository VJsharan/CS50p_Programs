'''Problem : To find out if the given fruit is in the given list and print its calories

Solution : Pretty ez done by using a for loop to traverse thru the entire dict and check if its in the dict and display its value using the func
'''
fruits_data = {
        "apple": "130",
        "avocado": "50",
        "banana": "110",
        "cantaloupe": "50",
        "grapefruit": "60",
        "grapes": "90",
        "honeydew melon": "50",
        "kiwifruit": "90",
        "lemon": "15",
        "lime": "20",
        "nectarine": "60",
        "orange": "80",
        "peach": "60",
        "pear": "100",
        "pineapple": "50",
        "plums": "70",
        "strawberries": "50",
        "sweet cherries": "100",
        "tangerine": "50",
        "watermelon": "80"
        }
fruit=input("Item :").lower()
for i in fruits_data:
    if i in fruits_data and i==fruit:
        print(f"Calories: {fruits_data[i]}")
