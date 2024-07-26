#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#
#Code is here : 

def simpleArraySum(ar):
    # 1: Take a variable named sum and store an initial value as 0.
    sum=0
    # 2 : Iterate a for loop through the given array.
    for num in ar : 
        #3 : Add up each array element in the sum variable 
        sum +=num
    # 4 : Return the sum variable after adding all the array elements.
    return sum   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

