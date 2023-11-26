
#count the vowels.
def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

#get the input from the user.
string = input("Enter any name ")
vowel_count = count_vowels(string)

#now count the vowels from the name given by the user.
print(f"The number of vowels in '{string}' is: {vowel_count}")
