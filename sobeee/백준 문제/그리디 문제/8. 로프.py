# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 13:27:05 2022

@author: bhs89
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