# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Validate the input
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize the row counter
    row = 0

    # Use a while loop to iterate through each row of the pattern
    while row < size:
        # Use a for loop to print asterisks side by side
        for _ in range(size):
            print("*", end="")
        
        # Print a newline character to move to the next row
        print()
        
        # Increment the row counter
        row += 1