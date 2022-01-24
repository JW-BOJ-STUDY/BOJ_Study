#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 19:14:18 2022

@author: baehongseob
"""

import sys

def input():
    return sys.stdin.readline().strip()

N = int(input())

weight_list = []

for i in range(N):
    weight = int(input())
    weight_list.append(weight)
    
weight_list.sort()

for i in range(N):
    if len(weight_list) == 1: #마지막 한개 남았을때
        max_weight = weight_list[0]
    elif weight_list[0] * len(weight_list) <= weight_list[1] * (len(weight_list)-1):
        weight_list.pop(0)
    else:
        max_weight = min(weight_list) * len(weight_list)

print(max_weight)

'''답지
N = int(input())
rope = []
value = []

for i in range(N):
    rope.append(int(input()))
rope.sort(reverse=True)

for num in range(N):
    value.append(rope[num]*(num+1))
    
print(max(value))
'''