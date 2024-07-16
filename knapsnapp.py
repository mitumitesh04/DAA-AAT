import math
import os
import random
import re
import sys

def unboundedKnapsack(k, arr):
    dp = [0] * (k + 1)
    
    for num in arr:
        for j in range(num, k + 1):
            dp[j] = max(dp[j], dp[j - num] + num)
    
    return dp[k]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        arr = list(map(int, data[idx:idx + n]))
        idx += n
        
        result = unboundedKnapsack(k, arr)
        results.append(result)
    
    for result in results:
        print(result)
