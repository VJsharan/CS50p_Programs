'''
The program's purpose:
- This program is designed to take an input date and output it in the YYYY-MM-DD format. It handles two types of date inputs:
--- Numeric format (MM/DD/YYYY).
--- Month-Day-Year format (Month Day, Year), where the month is in text (like "September").

#code explanation 
• The program starts by prompting the user to input a date in either `MM/DD/YYYY` or `Month Day, Year` format.  
• It enters an infinite loop (`while True`) to continuously process the input until a valid date format is provided.  
• If the input contains a `/`, the program assumes it is in the `MM/DD/YYYY` format and splits the input into month, day, and year.  
• It then verifies that both the day and month are numeric values.  
• It checks if the day is less than or equal to 31 and the month is less than or equal to 12.  
• If the checks pass, the program formats the date into `YYYY-MM-DD` format, ensuring the month and day are two digits, and prints it.  
• If the input contains a space and a comma (indicating the `Month Day, Year` format), the program splits the input into the month and the remaining day/year part.  
• The program removes any commas from the day part and ensures the day is numeric and the month is alphabetic.  
• It checks if the month is valid by verifying it is present in the `months_list` and that the day is valid (≤ 31).  
• If the input is valid, it formats and prints the date in the `YYYY-MM-DD` format, where the month is the corresponding index from the `months_list` and ensures the day is two digits.  
• The loop continues until a valid date format is entered and successfully printed.  
'''
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
'''
jeichitom maara finally
'''
while True:
    given=input("Date: ").strip()
    if '/' in given:
        month,day,year=given.split('/')
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
