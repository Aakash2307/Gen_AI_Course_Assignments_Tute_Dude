# Task 6: Read File Safely

# 1. Ask the user for a filename to open.

import os

filename = input("Enter filename: ")

# 2. If the file exists, read and print it.
# 3. If it does not exist, print:
# "File not found. Please check the filename."

if os.path.exists(filename):

    file = open(filename, "r")

    print(file.read())

    file.close()

else:
    print("File not found. Please check the filename.")