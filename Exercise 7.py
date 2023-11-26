
# Get the number from the user
number = int(input("Enter a number: "))

# Initialize variables
reversed_number = 0
remainder = 0

# Reverse the number using a while loop
while number > 0:
    remainder = number % 10
    reversed_number = (reversed_number * 10) + remainder
    number = number // 10

# Print the reversed number
print("Reversed number:", reversed_number)