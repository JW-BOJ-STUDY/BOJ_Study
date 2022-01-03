# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 01:26:56 2021

@author: bhs89
"""


import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())


for i in range(N):
    _str = input()
    cnt = 0
    for c in _str:
        if c == '(':
            cnt += 1 
        else:
            cnt -= 1
            
            if cnt < 0: #여기서 NO를 처리해버리면 cnt가 양수인건 처리가 안된다
                break 
            #break가 반복문 빠져나가면 밖에서 중복처리가 됨.

    if cnt == 0:
        print("YES")
    else:
        print("NO")

'''        내 첫 코딩
import sys

n = int(sys.stdin.readline().strip())
r_str = []

for i in range(n):
    _str = list(sys.stdin.readline().strip())
    for j in range(len(_str)):
        if _str[j] == "(":
            r_str.append("(")
        else:
            if len(r_str) == 0:
                print("NO")
            else:
                r_str.pop()
'''