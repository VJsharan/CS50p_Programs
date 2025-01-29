#unfisnihed
amount_due=50
inputs=[25,10,5]
print("Amount Due:",amount_due)
while(amount_due>=-1):
    if(amount_due==0):
        print("Change Owed:",amount_due)
        quit()
    coin=int(input("Insert Coin: "))
    if coin in inputs:
        amount_due-=coin
        print("Amount Due:",amount_due)
    else:
        print("Amount Due:",amount_due)


