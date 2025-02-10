months_list = [
    "xtra",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    given=input("Date: ")
    if '/' in given:
        month,day,year=given.split('/')
        year=year.strip()
        if day.isdigit() and month.isdigit():
            if int(day)<=31 and int(month)<=12:
                    print(f"{year}-{int(month):02}-{int(day):02}")
                    break
    elif " " and "," in given:
        month,day,year=given.split(' ')
        day=day.replace(',','')
        if day.isdigit() and month.isalpha():
                if int(day)<=31 and month in months_list:
                    print(f"{year.strip()}-{months_list.index(month):02}-{int(day):02}")
                    break
    else:
        continue
