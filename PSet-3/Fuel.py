'''
The program will calculate the percentage of fuel and output:
'F' if the fraction is almost full (≥ 99%),
'E' if the fraction is almost empty (≤ 1%),
A rounded percentage (e.g., "75%"), if the fraction is between 1% and 99%.
If the input is invalid (e.g., "3/0" or "abc/xyz"), the program will ask for the fraction again. 

# CODE Line by Line Explanation:
• The program starts by prompting the user to input a fraction (e.g., "3/4").
• It calls the frac() function and passes the user input to it for further processing.
• The frac() function begins by entering an infinite loop (while True) to repeatedly process the input until a valid result is returned.
• It attempts to split the input string by the / character into two parts: the numerator and the denominator
• It converts these two parts into integers for further calculations.
• The program calculates the percentage of the fraction by dividing the numerator by the denominator and multiplying the result by 100.
• It checks if the fraction is invalid by verifying:
• If the numerator is greater than the denominator (e.g., "4/3"),
• If the calculated percentage is above 100% or below 0% (which would be invalid).
• If any of the above conditions are true, it does nothing and continues to the next iteration of the loop.
• If the percentage is greater than or equal to 99%, it returns "F", indicating the fuel tank is full.
• If the percentage is less than or equal to 1%, it returns "E", indicating the fuel tank is empty.
• If the percentage is valid and between 1% and 99%, it rounds the percentage to the nearest integer and returns it as a string, followed by the percentage sign (%).
• If the input is invalid (e.g., a non-numeric input or division by zero), it catches the error using a try-except block.
• If any error is encountered (such as ValueError or ZeroDivisionError), the program skips to the next iteration of the loop and asks for input again.
• The loop continues asking for a valid fraction until it successfully processes the input and returns the correct output.
'''

def main():
    given=input("Fraction: ")
    print(frac(given))

def frac(given):
    while True:
        try:
            x,y=given.split("/")
            x,y=int(x), int(y)
            percent=float((x / y) * 100)
            if int(x)>int(y) or percent>100 or percent<0:
                pass
            elif percent>=99:
                return 'F'
            elif percent<=1:
                return 'E'
            else:
                return f"{round(percent)}%"
                break
        except (ValueError, ZeroDivisionError):
            continue

main()
