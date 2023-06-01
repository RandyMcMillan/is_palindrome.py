#!/usr/bin/env python3

import operator


# 𝐴⊕𝐵=𝐴𝐵′+𝐴′𝐵
global xor
xor = -1


def test():
    # Initializing two integer variables
    #print("type(xor)=%s",type(xor))
    a = xor
    b = 0
    
    # Printing a and b before swapping
    print("a before swap =", a)
    print("b before swap =", b)
    
    print()
    
    # Swapping a and b using XOR operator
    a = a ^ b
    b = a ^ b
    a = a ^ b
    
    # Printing a and b after swapping using XOR
    print("a after swap =", a)
    print("b after swap =", b)
    
    # exit();

# define a function to check if a number is a palindrome
def is_palindrome(n):
    # convert the number to a string
    s = str(n)
    
    # check if the string is the same forwards and backwards
    # return s == int(s[::-1])
    return s == s[::-1]

# define the start and end of the range
start = 0
end = 21111112

# create an empty list to store the palindromes
palindromes = []

# loop through the range of numbers
for n in range(start, end+1):

    # if the number is a palindrome, add it to the list
    #  print("n=%d" % n)
    if is_palindrome(n):

        #n = int(n)
        #print("type(n)=%s",type(n))
        palindromes.append(n)

        # print("len(palindromes)=%d" % len(palindromes))
        if len(palindromes) > -1:

            # print("palindromes[ int(len(palindromes)-2) ]=%d" % palindromes[ int(len(palindromes)-2) ])
            # print("palindromes[ int(len(palindromes)-1) ]=%d" % palindromes[ int(len(palindromes)-1) ])

            # xor = palindromes[ len(palindromes)-1 ] ^ palindromes[len(palindromes)-2]
            # test()
            # print("pre:^=%d" % xor)
            # xor = palindromes[ int(len(palindromes)-1) ] ^ palindromes[ int(len(palindromes)-2) ]
            # xor = palindromes[ int(len(palindromes)-2) ] ^ palindromes[ int(len(palindromes)-1) ]
            xor = palindromes[ int(len(palindromes)-2) ] ^ palindromes[ int(len(palindromes)-1) ]
            # print("type(xor)=%s",type(xor))
            # test()
            print("%d^" % palindromes[ int(len(palindromes)-2) ]+"%d" % palindromes[ int(len(palindromes)-1) ]+"=%d" % xor)
            #print("^=%d" % xor)
            # test()

            # xor = operator.xor(palindromes[ len(palindromes)-2 ], palindromes[len(palindromes)-1])
            # xor = operator.xor(palindromes[ len(palindromes)-1 ], palindromes[len(palindromes)-2])
            # print("xor=%d" % xor)

# print the list of palindromes
# print(palindromes)
