
#get the number from the user.
num_terms = int(input("Enter the number of terms "))

# Initialize the first two terms of the series
first_term = 0
second_term = 1

# Print the first two terms
print(first_term)
print(second_term)

# Generate the remaining terms using a for loop
for i in range(2, num_terms):
    next_term = first_term + second_term
    print(next_term)
    
    # Update the values of first_term and second_term
    first_term = second_term
    second_term = next_term