# Assignment 8: File Handling

# Open the input file in read mode
with open("input.txt", "r") as file:
    lines = file.readlines()

# Count the number of lines
line_count = len(lines)

# Display the line count
print("Total number of lines:", line_count)

# Extract the first two lines
first_two_lines = lines[:2]

# Write the first two lines into a new file
with open("output.txt", "w") as file:
    file.writelines(first_two_lines)

print("First two lines have been written to output.txt")

