#!/usr/bin/env python3
    
import operator
from hashlib import sha256
import string
import re
from ast import literal_eval
import json
    
# 𝐴⊕𝐵=𝐴𝐵′+𝐴′𝐵
global xor
    
# initialize lists
global palindromes
palindromes = []
global xor_results
xor_results = []
global xor_palindromes
xor_palindromes = []
global hash_palindromes
hash_palindromes = []

# define a function to check if a number is a palindrome
def is_palindrome(n):
    
    # convert the number to a string
    s = str(n)
    
    # check if the string is the same forwards and backwards
    return s == s[::-1]

def do_it(_input):
    
    # define the start and end of the range
    start = -1
    end = int(_input)
    
    # loop through the range of numbers
    for n in range(start, end + 1):
    
        # if the number is a palindrome, add it to the list
        if is_palindrome(n):
    
            palindromes.append(n)
            if len(palindromes) > -1:
    
                xor = palindromes[ int(len(palindromes)-2) ] ^ palindromes[ int(len(palindromes)-1) ]
                xor_results.append(n)
    
                # print("type(xor)=%s",type(xor))
                print("%d^" % palindromes[ int(len(palindromes)-2) ] +
                    "%d" % palindromes[ int(len(palindromes)-1) ] +
                    "=%d" % xor)
    
                if is_palindrome(xor):
    
                    # palindromes.append(xor)
                    if is_palindrome(sha256(str(xor).encode('utf-8')).hexdigest()):
                        hash_palindromes.append(xor)
                        # unlikely but...
                        print(sha256(str(xor).encode('utf-8')).hexdigest())
    
                    # if the resulting xor is a palindrome
                    # we append to the xor_palindrome list
                    xor_palindromes.append(xor)
    
    # write for each iteration
    save_to_files()

def is_hex(s):
    
    return re.fullmatch(r"^[0-9a-fA-F]$", s or "") is not None
    
def is_hex_str(s):
    
    return set(s).issubset(string.hexdigits)
    
    
def check_user_input(input_):
    
    try:
        # Convert it into integer
        val = int(input_)
        do_it(val)
    
    except ValueError:
    
        if is_hex(input_):
            try:
                print("is_hex:hex value? %s" % input_)
                res = int(input_,16)
                print("is_hex:hex value? %s" % res)
                do_it(res)
                exit()
            finally:
                False
        if is_hex_str(input_):
            try:
                print("is_hex_str:hex value? %s" % input_)
                res = int(input_,16)
                print("is_hex_str:hex value? %s" % res)
                do_it(res)
                exit()
            finally:
                False
        try:
            # Convert it into float
            val = float(input_)
            print("Input is a float  number. Number = ", val)
            exit()
        except ValueError:
            try:
                res = literal_eval(input_)
                print("ValueError:\nThe resultant integer is ")
                print(res)
                do_it(res)
                exit()
            finally:
                print("No.. input is not a number. It's a string")
    
    
def save_to_file(title, text):
    
    with open(str(title), mode='wt', encoding='utf-8') as myfile:
        myfile.write(''.join(str(text)))
    
    
def save_to_files():
    
    # print the list of palindromes
    
    # print("palindromes")
    # print(palindromes)
    save_to_file("palindromes", palindromes)
    
    # print("xor_results")
    # print(xor_results)
    save_to_file("xor_results", xor_results)
    
    # print("xor_palindromes")
    # print(xor_palindromes)
    save_to_file("xor_palindromes", xor_palindromes)
    
    # print("hash_palindromes")
    # print(hash_palindromes)
    save_to_file("hash_palindromes", hash_palindromes)
    
    
input_ = input('Enter something (default 999999):\n')
if input_ == "":
    input_ = 999999
    
check_user_input(input_)
