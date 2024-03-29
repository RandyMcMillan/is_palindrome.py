#!/usr/bin/env python3
import sys

# define a function to check if a number is a palindrome
def is_palindrome(n):
    # convert the number to a string
    s = str(n)
    # check if the string is the same forwards and backwards
    return s == s[::-1]

def loop(lb, ub):

    # define the start and end of the range
    start = int(lb)
    end = int(ub)

    # create an empty list to store the palindromes
    palindromes = []

    # loop through the range of numbers
    for n in range(start, end+1):
        # if the number is a palindrome, add it to the list
        if is_palindrome(n):
            palindromes.append(n)

    # print the list of palindromes
    if len(palindromes) > 0:
        print(palindromes)
        hexlist = list(map(hex, palindromes));
        if len(hexlist) > 0:
            ## print(hexlist)
            print('[{}]'.format(', '.join(str(x)[2:] for x in hexlist)))

if (args_count := len(sys.argv)) == 3:

    if int(sys.argv[1]) > int(sys.argv[2]):
        ## print("int(sys.argv[1]) > int(sys.argv[2])");
        lower_bound = int(sys.argv[2]);
        upper_bound = int(sys.argv[1]);
        loop(lower_bound, upper_bound)

    if int(sys.argv[1]) < int(sys.argv[2]) or int(sys.argv[1]) == int(sys.argv[2]):
        ## print("int(sys.argv[1]) < int(sys.argv[2])");
        lower_bound = int(sys.argv[1]);
        upper_bound = int(sys.argv[2]);
        loop(lower_bound, upper_bound)

elif args_count == 2:

    if int(sys.argv[1]) > int(sys.argv[2]):
        print("int(sys.argv[1]) > int(sys.argv[2])");
        lower_bound = int(0);
        upper_bound = int(sys.argv[2]);
        loop(lower_bound, upper_bound)

    if int(sys.argv[1]) < int(sys.argv[2]):
        print("int(sys.argv[1]) < int(sys.argv[2])");
        lower_bound = int(0);
        upper_bound = int(sys.argv[1]);
        loop(lower_bound, upper_bound)


elif args_count > 2:

    print("Usage:\n")
    print("is_palindrome <int>\n")
    print("is_palindrome <int> <int>\n")
    raise SystemExit(0)

elif args_count < 2:

    print("Usage:\n")
    print("is_palindrome <int>\n")
    print("is_palindrome <int> <int>\n")
    raise SystemExit(0)
