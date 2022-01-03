# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 20:55:02 2022

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline()

N = int(input())
move = list(input().split())
x = 1
y = 1

for i in move:
    if i == L:
        if x == 1:
            continue
        else:
            x -= 1
    elif i == R:
        if x == len(move):
            continue
        else:
            x+=1
    elif i == U:
        if y == 1:
            continue
        else:
            y-=1
    elif i == D:
        if y == len(move):
            continue
        else:
            y+=1

print(x+" "+y)