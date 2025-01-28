#just a lil bit complex, it takes the given time from user as the string, and splits it into hr and mins as : as the separator
#then its converted into float by taking the hr and adding it to the minute/60 since if its 7:30, 7.00 + 30/60 gives 0.5, so 7.5
# so we have 7:30 as 7.5, and its checked at what range it falls in and displayed whether its dinner or lunch or breakfast time
# more info https://www.youtube.com/watch?v=pU2qzo8NOkA&ab_channel=TheCodingCreator
def main():
    time=input("What time is it? ")
    x=(convert(time))
    if x>=7.00 and x<=8.00:
        print("breakfast time")
    elif x>=12.00 and x<=13.00:
        print("lunch time")
    elif x>=18.00 and x<=19.00:
        print("dinner time")

def convert(time):
    hrs,min=time.split(":")
    hrs=float(hrs) + (float(min)/60)
    return hrs

if __name__ == "__main__":
    main()
