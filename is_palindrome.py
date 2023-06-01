#!/usr/bin/env python3

import operator
from hashlib import sha256
import string
import re
from ast import literal_eval

#def is_hex_str(s):
#    return set(s).issubset(string.hexdigits)



# 𝐴⊕𝐵=𝐴𝐵′+𝐴′𝐵
global xor
xor = 0

# create an empty list to store the palindromes
global palindromes
palindromes = []


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
    return s == s[::-1]

def do_it(_input):

    # define the start and end of the range
    start = 0
    end = int(_input)
    
    # loop through the range of numbers
    for n in range(start, end + 1):
    
        # if the number is a palindrome, add it to the list
        if is_palindrome(n):

            # print("n=%s" % sha256(str(n).encode('utf-8')).hexdigest())
    
            # print("n=%d" % n)
            # print("type(n)=%s",type(n))
            palindromes.append(n)
            if len(palindromes) > -1:
    
                xor = palindromes[ int(len(palindromes)-2) ] ^ palindromes[ int(len(palindromes)-1) ]
    
                # print("type(xor)=%s",type(xor))
                print("%d^" % palindromes[ int(len(palindromes)-2) ] +
                    "%d" % palindromes[ int(len(palindromes)-1) ] +
                    "=%d" % xor)
    
                if is_palindrome(xor):
                    # palindromes.append(xor)
                    if is_palindrome(sha256(str(xor).encode('utf-8')).hexdigest()):
                        palindromes.append(xor)
                        # print(sha256(str(xor).encode('utf-8')).hexdigest())

def is_hex(s):
    return re.fullmatch(r"^[0-9a-fA-F]$", s or "") is not None

def is_hex_str(s):
    return set(s).issubset(string.hexdigits)


def check_user_input(input_):
    try:
        # Convert it into integer
        val = int(input_)
        # print("Input is an integer number. Number = ", val)
        do_it(val)

    except ValueError:

        if is_hex(input_):
            try:
                print("is_hex:hex value? %s" % input_)
                res = int(input_,16)
                print("is_hex:hex value? %s" % res)
                do_it(res)
                ## TODO convert to decimal
            finally:
                False
        if is_hex_str(input_):
            try:
                print("is_hex_str:hex value? %s" % input_)
                res = int(input_,16)
                print("is_hex_str:hex value? %s" % res)
                do_it(res)
                # print("is_hex_str:hex value? %s" % res)
                ## TODO convert to decimal
            finally:
                False
        try:
            # Convert it into float
            val = float(input_)
            print("Input is a float  number. Number = ", val)
            do_it(val)
        except ValueError:
            try:
                res = literal_eval(input_)
                print("ValueError:\nThe resultant integer is ")
                print(res)
                do_it(res)
            finally:
                print("No.. input is not a number. It's a string")


input_ = input('Enter something (default 999):\n')
if input_ == "":
    input_ = 999

check_user_input(input_)


# print the list of palindromes
print(palindromes)
