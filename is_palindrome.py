#!/usr/bin/env python3

# define a function to check if a number is a palindrome
def is_palindrome(n):
    # convert the number to a string
    s = str(n)
    
    # check if the string is the same forwards and backwards
    return s == s[::-1]

# define the start and end of the range
start = 1
end = 1000001

# create an empty list to store the palindromes
palindromes = []

# loop through the range of numbers
for n in range(start, end+1):
    # if the number is a palindrome, add it to the list
    if is_palindrome(n):
        palindromes.append(n)

# print the list of palindromes
print(palindromes)
