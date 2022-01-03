# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 20:20:44 2021

@author: bhs89
"""

import sys

def push(x):
    _list.append(x)
    
def pop():
    if len(_list) == 0:
        return print(-1)
    print(_list.pop())


def size():
    return print(len(_list))        

def empty():
    if len(_list) == 0:
        print(1)
    else:
        print(0)
    
def top():
    if len(_list) == 0:
        print(-1)
    print(_list[-1])
    
#-----------main-----------
"""def input():
    return sys.stdin.readline().strip()
_list = []

n = int(input())
num = 0

for i in range(n):
    _input = input().split()
    
    if len(_input) == 2:
        num = _input[1]
    _input = _input[0]
    
    if _input == 'push':
        push(num)
    elif _input == 'pop':
        pop()
    elif _input == "size":
        size()
    elif _input == "empty":
        empty()
    elif _input == "top":
        top() """
_list = []        
push(1)
push(2)
top()
size()
empty()
pop()
pop()
pop()
size()
empty()
pop()
push(3)
empty()
top()