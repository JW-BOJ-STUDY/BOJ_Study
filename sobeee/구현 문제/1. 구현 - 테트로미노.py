# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 23:50:13 2022

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline().strip()

#Rectangle 직사각형 배열
def checkBox(Rectangle,i,j):
    
    # ㅡ ㅣ 모양
    try:
        _straight1 = Rectangle[i][j] + Rectangle[i+1][j] +Rectangle[i+2][j] +Rectangle[i+3][j]
    except:
        _straight1 = 0
    try:
        _straight2 = Rectangle[i][j] +Rectangle[i][j+1] +Rectangle[i][j+2] +Rectangle[i][j+3]
    except:
        _straight2 = 0
    # ㅁ 모양
    try:
        _square = Rectangle[i][j] +Rectangle[i+1][j] +Rectangle[i][j+1] +Rectangle[i+1][j+1]
    except:
        _square = 0
    # L 모양 (회전 ㅇ)
    try:
        _L1 = Rectangle[i][j] +Rectangle[i+1][j] +Rectangle[i+2][j] +Rectangle[i+2][j+1]
    except:
        _L1 = 0
    try:
        _L2 = Rectangle[i][j] +Rectangle[i+1][j] +Rectangle[i][j+1] +Rectangle[i][j+2]
    except:
        _L2 = 0
    try:
        _L3 = Rectangle[i][j] +Rectangle[i][j+1] +Rectangle[i+1][j+1] +Rectangle[i+2][j+1]
    except:
        _L3 = 0
    try:
        _L4 = Rectangle[i][j] +Rectangle[i][j+1] +Rectangle[i][j+2] +Rectangle[i-1][j+2]
    except:
        _L4 = 0
    try:
        _L5 = Rectangle[i][j] +Rectangle[i][j+1] +Rectangle[i-1][j+1] +Rectangle[i-2][j+1]
    except:
        _L5 = 0
    try:
        _L6 = Rectangle[i][j] +Rectangle[i+1][j] +Rectangle[i+1][j+1] +Rectangle[i+1][j+2]
    except:
        _L6 = 0
    try:
        _L7 = Rectangle[i][j] +Rectangle[i][j+1] +Rectangle[i+1][j] +Rectangle[i+2][j]
    except:
        _L7 = 0
    try:
        _L8 = Rectangle[i][j] +Rectangle[i][j+1] +Rectangle[i][j+2] +Rectangle[i+1][j+2]
    except:
        _L8 = 0
    try:
        _lightning1 = Rectangle[i][j] +Rectangle[i+1][j] +Rectangle[i+1][j+1] +Rectangle[i+2][j+1]
    except:
        _lightning1 = 0
    try:
        _lightning2 = Rectangle[i][j] +Rectangle[i][j+1] +Rectangle[i-1][j+1] +Rectangle[i-1][j+2]
    except:
        _lightning2 = 0
    try:
        _lightning3 = Rectangle[i][j] +Rectangle[i+1][j] +Rectangle[i+1][j-1] +Rectangle[i+2][j-1]
    except:
        _lightning3 = 0
    try:
        _lightning4 = Rectangle[i][j] +Rectangle[i][j+1] +Rectangle[i+1][j+1] +Rectangle[i+1][j+2]
    except:
        _lightning4 = 0
    # ㅗ 모양
    try:
        _fuck1 = Rectangle[i][j] +Rectangle[i+1][j-1] +Rectangle[i+1][j] +Rectangle[i+1][j+1]
    except:
        _fuck1 = 0
    try:
        _fuck2 = Rectangle[i][j] +Rectangle[i+1][j] +Rectangle[i+1][j+1] +Rectangle[i+2][j]
    except:
        _fuck2 = 0
    try:
        _fuck3 = Rectangle[i][j] +Rectangle[i][j+1] +Rectangle[i+1][j+1] +Rectangle[i][j+2]
    except:
        _fuck3 = 0
    try:
        _fuck4 = Rectangle[i][j] +Rectangle[i][j+1] +Rectangle[i-1][j+1] +Rectangle[i+1][j+1]
    except:
        _fuck4 = 0
    
    return max(_straight1,_straight2,_square,_L1,_L2,_L3,_L4,_L5,_L6,_L7,_L8,_lightning1,_lightning2,_lightning3,_lightning4,_fuck1,_fuck2,_fuck3,_fuck4)
N, M = map(int, input().split())

Rectangle = []
_max = 0
for i in range(N):
    row = list(map(int, input().split()))
    Rectangle.append(row)

for i in range(N):
    for j in range(M):
        _max = max(_max,checkBox(Rectangle, i, j))
        
print(_max)