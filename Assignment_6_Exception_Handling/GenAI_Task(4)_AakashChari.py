# Task 4: File Reader with Exception Handling

# 1. Ask the user for a filename.

filename = input("Enter Filename: ")

try:

    # 2. Try to open and read the file.

    file = open(filename, "r")

    lines = file.readlines()

# 3. Handle FileNotFoundError

except FileNotFoundError:
    print("File not found.")

# Handle PermissionError

except PermissionError:
    print("Permission denied.")

else:

    # 4. If successful, print first 3 lines of the file.

    print("First 3 Lines:")

    for line in lines[:3]:
        print(line.strip())

    file.close()

finally:

    # 5. Use finally to print:

    print("File operation attempted.")