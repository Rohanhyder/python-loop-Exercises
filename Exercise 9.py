def is_palindrome(number):
    temp = number
    reverse = 0

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10

    if number == reverse:
        return True
    else:
        return False

# Taking user input
num = int(input("Enter a number: "))

if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
