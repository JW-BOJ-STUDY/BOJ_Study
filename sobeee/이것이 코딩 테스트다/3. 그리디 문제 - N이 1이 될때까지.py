# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 20:05:20 2022

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline()

# N을 1로 만들기
# 1. N-1
# 2. N / K -> 나누어 떨어질때만 사용가능

N, K = map(int, input().split())
count = 0

while(N != 1):
    if (N % K) == 0:
        N = N / K
        count += 1
    
    else:
        N = N-1
        count += 1
        
print(count)
        
#답지
'''
n, k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k
    result = result + (n-target) # k의 배수될때까지 n-1 진행
    n = target
    
    if n < k :
        break
    
    result += 1
    n //= k
    
result += (n-1) #나머지에 대해 n이 1이 될때까지 진행
print(result)
'''