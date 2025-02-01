'''Problem : To check whether a license plate follows the rules for vanity plates. 
The rules for a valid plate are:

The plate must have between 2 and 6 characters.
The plate must start with two alphabetic characters.
The plate can contain only letters and digits (alphanumeric).
The plate cannot start with a '0'.
Once a digit appears, no letters should follow.
The program should prompt the user to input a license plate and then print "Valid" if the plate adheres to all rules, or "Invalid" if any of the rules are violated.

CODE line by line explanation:
• It starts by prompting the user to input a license plate.
• It calls the is_valid() function to check if the entered plate follows the rules.
• If the plate is valid according to is_valid(), it prints "Valid".
• If the plate doesn't meet the rules, it prints "Invalid".
• The is_valid() function first checks if the length of the plate is between 2 and 6 characters.
• It checks if the first two characters of the plate are alphabetic.
• It ensures that the plate contains only alphanumeric characters (letters and digits).
• It initializes a variable first_found to track if a digit has been encountered.
• The program then iterates over each character of the plate.
• If the first character is '0', the plate is invalid and returns False.
• If the plate has already encountered a digit and a letter is found afterward, it returns False.
• If a digit is encountered, it marks that a digit has started by setting first_found to True.
• If all checks pass, it returns True, indicating the plate is valid.
• If any check fails, it returns False, marking the plate as invalid.'''

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
        first_found = False
        for index, character in enumerate(s):
            if character == '0' and index == 0:
                return False
            if first_found and character.isalpha():
                return False
            if character.isdigit():
                first_found = True
        return True
    else:
        return False

main()
