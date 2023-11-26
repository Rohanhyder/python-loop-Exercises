
# get number from the user.
num = int(input("Enter a number "))

# Initializing the factorial variable
factorial = 1

# Calculating the factorial using a while loop
while num > 0:
    factorial *= num
    num -= 1

print("The factorial of the number is:", factorial)
