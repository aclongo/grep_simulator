# Write a simple program to simulate the operation of the
# grep command on Unix. Ask the user to enter a regular expression and
# count the number of lines that matched the regular expression:
    # $ python3 grep.py
    # Enter a regular expression: ^Author
    # mbox.txt had 1798 lines that matched ^Author

# Ask user for a txt file name and save in fname variable
# Open the txt file with a file handle
# Use try and except to prevent bad file names
# Ask user for a regular expression and save in regex variable
# Initialize a line counter
# Perform the regex on each line using a for loop
# Increment the line counter when matches are found (list not empty)
# Print an f-string using file name, line counter and regex variables