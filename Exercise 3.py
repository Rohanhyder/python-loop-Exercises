
# get the number from the user.
num = int(input("Enter a number: "))

# now add the natural number to the given number.
sum = 0
i = 1

while i <= num:
    sum += i
    i += 1

print("The sum of natural number up to", num, "is", sum)