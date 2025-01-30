''' CODE line by line explanation
PROBLEM : Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these
denominations: 25 cents, 10 cents, and 5 cents. In a file called coke.py, implement a program that prompts the user to insert a coin,
one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many
cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

• It initially starts with amount due as 50.
• The allowed inputs are in a list.
• Prints the initial due amount.
• Goes into the while loop, only if the amount is >= 0.
• Then checks if it's = to 0.
• If yes, then prints the change owed as 0 and quits.
• Then going into the while, asks for coin from user.
• Checks if the coin is in allowed inputs.
• Then checks if the inputted coin is greater than the due.
• If it is greater, then prints the change owed by the machine to the user, (coin 25, due 10, performs COIN - DUE, change to user = 25 - 10 -> 15) and then quits it.
• If the input coin is lesser than due, then subtracts, due - coin and prints due amount.
• Lastly prints due amount at the end of each iteration.
'''

inputs=[25,10,5]
print("Amount Due:",amount_due)
while(amount_due>=0):
    if(amount_due==0):
        print("Change Owed:",amount_due)
        quit()
    coin=int(input("Insert Coin: "))
    if coin in inputs:
        if coin>amount_due:
            print("Change Owed:",coin-amount_due)
            quit()
        else:
            amount_due-=coin
            print("Amount Due:",amount_due)
    else:
        print("Amount Due:",amount_due)


