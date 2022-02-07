# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 22:36:42 2022

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline().strip()

N, M = map(int,input().split())
square = []
ans = 1 #default 값 1

# 직사각형 만들기
for i in range(N):
    row = list(map(int,input().split()))
    square.append(row)

for i in range(N):
    for j in range(M):
        vertex1 = square[i][j]
        square[i][j] = 100
        if vertex1 not in square[i]:
            continue
        else:
            interval = square[i].index(vertex1) - j
            
            #vertex1,2,3,4 (위)왼오 (아래)왼오
            
            # vertex3 왼쪽 아래 꼭짓점이 배열 index 초과
            if i + interval >= N: 
                continue
            else:
                #vertex1 = square[i][j]
                vertex2 = square[i][j+interval]
                vertex3 = square[i+interval][j]
                vertex4 = square[i+interval][j+interval]
                
                if vertex1 == vertex2 == vertex3 == vertex4:
                    ans = max(ans, (interval+1)*(interval+1))
print(ans)