# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # count = 0
    # n = len(candles)
    # tallest = max(candles)
    # for i in range(0,n):
    #     if candles[i] == tallest:
    #         count +=1
    # return count
    
    # Write your code here
    return candles.count(max(candles))

print('The tallest candles count is ', birthdayCakeCandles([4,3,4,4,5,3,3,4,5,5,3,3,5,4,3,5,5,3,5,4,1,2,3]))