# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 20:56:41 2021

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline().strip()

n, k = map(int, input().split())
#n, k = int(input().split())

walk = k-1 #출력할 k번째인덱스 -> walk로 표현
_list = [i+1 for i in range(n)]
result = []

while (n!=0):
    result.append(_list.pop(walk))
    n = n-1
    if n == 0: #_list의 크기가 0일때까지만 반복
        break
    # mod 연산을 이용하여 index 지정
    if walk-1 < 0:
        walk = n-1
        walk = (walk+k)%n
    else:
        walk = (walk-1)%n # pop 이후 줄어든 list의 크기 반영
        walk = (walk+k)%n # walk 위치에서 다시 k번째로 index 이동
    
print('<' + ', '.join(map(str, result)) + '>')

