# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 23:44:58 2022

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline()

N, M = map(int, input().split())

arr = list(map(int, input().split()))
minimum_max = min(arr)

for i in range(N):
    arr_example = list(map(int, input().split()))
    mini_example = min(arr_example)
    
    if minimum_max < mini_example:
        minimum_max = mini_example
        
print(minimum_max)