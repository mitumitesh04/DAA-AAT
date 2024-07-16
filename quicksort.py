# import math
# import os
# import random
# import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def partition(arr):
    pivot = arr[0]
    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    
    return left + middle + right

def main():
    input = sys.stdin.read
    data = input().splitlines()
    n = int(data[0])
    arr = list(map(int, data[1].split()))

    result = partition(arr)
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    main()