#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 16:06:49 2022

@author: baehongseob
"""

'''
import sys
import math #math.pow(숫자, 지수) 사용

def input():
    return sys.stdin.readline().strip()

A, B = map(str, input().split())

a = '4' * len(A) # 4 min 값
b = '7' * len(B) # 77 max 값

# 전체 경우에서 여집합으로 가보자
entire = 0
a_long = len(a)

# A <= a , B>= b  인 경우. 4 ~ 77 모든게 가능할 때
for i in range(len(b)-len(a)+1): # +1로 if절 안쓰고 날려도 됨
    entire += math.pow(2,a_long)
    a_long+=1
    
# A > a 인 경우 -> 이때 A와 a의 자릿수는 같다
# 44 라면 A는 뭐 55 60 이런거

if int(A) > int(a):
    a_long = len(a)
    A = int(A)
'''

def dfs(lower,upper,depth,number):
    answer = 0
    if (depth>=10):
        return 0
    if number > upper:
        return 0
    if upper>= number >= lower:
        answer+= 1
        
    answer += dfs(lower,upper,depth+1,number*10+4)
    answer += dfs(lower,upper,depth+1,number*10+7)
    return answer

A,B = map(int,input().split())

ans = dfs(A,B,0,0)
print(ans)

'''답지
import sys
a,b = map(int,sys.stdin.readline().split())
cnt = 0
def solve(n):
    global cnt
    if n>b:
        return 0
    if a<=n<=b:
        cnt+=1
    solve(n*10+4)
    solve(n*10+7)
solve(4)
solve(7)
print(cnt)
'''