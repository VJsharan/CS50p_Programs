# problem : the initial price and tip% are given, then the amount is given after removing the 2nd digit after the decimal point, and also the tip% is found out by converting 15 -> 0.15 like that
# visit https://cs50.harvard.edu/python/2022/psets/0/tip/ for more info 
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return (float(d[1:-2]))


def percent_to_float(p):
    x=float(p[:-1])
    return (x/100)



main()
