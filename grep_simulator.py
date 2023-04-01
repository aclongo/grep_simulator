# Write a simple program to simulate the operation of the
# grep command on Unix. Ask the user to enter a regular expression and
# count the number of lines that matched the regular expression:
    # $ python3 grep.py
    # Enter a regular expression: ^Author
    # mbox.txt had 1798 lines that matched ^Author

import re

# Ask user for a txt file name and save in fname variable
while True:
    try:    
        fname = input('Enter the name of a txt file: ')
    # Open the txt file with a file handle
        fhand = open(fname)
        break
    # Use try and except to prevent bad file names
    except FileNotFoundError:
        print('File not found.')
        continue

# Ask user for a regular expression and save in regex variable
regex = input('Enter a regular expression: ')
# Initialize a line counter
line_count = 0

# Perform the regex on each line using a for loop
for line in fhand:
    match = re.findall(regex, line)
# Increment the line counter when matches are found (list not empty)
# Print an f-string using file name, line counter and regex variables