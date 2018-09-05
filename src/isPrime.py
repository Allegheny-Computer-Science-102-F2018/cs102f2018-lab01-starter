#!/usr/bin/env python3

# obonhamcarter@allegheny.edu
# date 31 Aug 2018

data = open("../input/dataFile.txt")
numOfPrimes_int = 0
numOfNonPrimes_int = 0
numOfNums_int = 0


for line_str in data:
    #print( "line_str : ",line_str)
    numOfNums_int += 1
    try: # if the line contains something other than an integer
        n_int = int(line_str)
    except ValueError: # catch the non-integer
        pass

    isPrime = True

    # TO DO: Complete the program to check primality

print("    Number of values in file   : ",numOfNums_int)
print("    Number of primes           : ",numOfPrimes_int)
print("    Number of composites        : ",numOfNonPrimes_int)
