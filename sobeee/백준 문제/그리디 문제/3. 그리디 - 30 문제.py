# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 23:01:18 2022

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline()

N = input().strip()

index = 0
result = 1
# N = 2931

for i in N:
    if i == '0':
        result = 0
        break
    index+=1

# N = 2931
N = N[:index] + N[index+1:]

if result != 0:
    print(-1)
else:
    if (int(N) % 3) == 0:
        N = sorted(N,reverse=True)
        N.append('0')
        result = ''.join(N)
        result = int(result)
        print(result)
    else:
        print(-1)