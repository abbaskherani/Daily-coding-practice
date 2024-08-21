#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(a):
    # Write your code here
    max_sum = float('-inf')
    for i in range(len(a) - 2):
        for j in range(len(a)-2):
            sum= a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] +a[i+2][j] + a[i+2][j+1] + a[i+2][j+2]
            if sum > max_sum:
                max_sum = sum
    return max_sum
    
# sum = []


# for i in range(len(arr)-2):
#     for j in range(len(arr)-2):
#         sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
        
# print(max(sum))
        
# maxSum = 0 
# for i in range(1,5): 
#     for j in range(1,5): 
#         maxSum = 
#         max(maxSum, (arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
