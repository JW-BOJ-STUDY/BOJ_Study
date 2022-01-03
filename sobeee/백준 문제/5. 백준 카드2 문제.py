# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 23:08:14 2021

@author: bhs89
"""
#list를 이용하여 구현. -> pop(0)와 append 연산 -> deque 사용
'''
import sys

def input():
    return sys.stdin.readline().strip()

N = int(input())

card_list = [i+1 for i in range(N)]

for i in range(N-1):
    if len(card_list) == 1:
        break
    
    first = card_list.pop(0)
    second = card_list.pop(0)
    
    card_list.append(second)
    
print(card_list[0])
'''
import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

N = int(input())

card_list = deque([i+1 for i in range(N)])

for i in range(N-1):
    if len(card_list) == 1:
        break
    
    first = card_list.popleft()
    second = card_list.popleft()
    
    card_list.append(second)
    
print(card_list.popleft())

'''
a,b=int(input()),1
while a>b:b*=2
print(a*2-b)
'''