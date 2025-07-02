# Problem: CS50P Figlet
# Goal: Create a program that renders user input text as ASCII art using a font, optionally specified via command-line arguments.
# If no font is specified, a random font is used.
# If invalid arguments are passed, the program exits with an error message.

import sys       # to access command-line arguments and exit the program
import random    # to choose a random font when one isn't specified
from pyfiglet import Figlet  # for generating ASCII art from text

# List of available fonts (you could use figlet.getFonts() to fetch them instead of hardcoding)
fonts = ['small', 'pyramid', '5x8', 'fender', 'graffiti', ...]  # truncated for readability

figlet = Figlet()  # Create a Figlet object to use for rendering ASCII text

# If the user provided two additional command-line arguments (e.g., -f slant)
if len(sys.argv) == 3:
    # Check if the first argument is a valid flag for specifying font
    if sys.argv[1] in ('-f', '--font'):
        # Set the font only if it's in the allowed list
        if sys.argv[2] in fonts:
            figlet.setFont(font=sys.argv[2])
            s = input("Input: ")  # Prompt user for text
            print(figlet.renderText(s))  # Output ASCII art
        else:
            print("Invalid Usage")  # Font name not in list
            sys.exit(1)  # Exit with error status
    else:
        print("Invalid Usage")  # Invalid flag
        sys.exit(1)  # Exit with error status

# If only one argument is given (which is incorrect usage), exit
elif len(sys.argv) == 2:
    print("Invalid Usage")  # User likely gave just a font name without flag
    sys.exit(1)  # Exit with error status

# If no font is specified, choose one randomly
elif len(sys.argv) == 1:
    f = random.choice(fonts)  # Pick a random font
    figlet.setFont(f)
    s = input("Input: ")  # Prompt user for input
    print(figlet.renderText(s))  # Output the rendered ASCII art

# Any other case (like more than 3 arguments), treat as invalid
else:
    print("Invalid Usage")
    sys.exit(1)
