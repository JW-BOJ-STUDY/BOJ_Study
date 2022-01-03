# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 02:59:19 2021

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline().strip()

N = int(input())
#Queue 구조 First in first out
result = [] #구조임 넣어야돼

for i in range(N):

    _str = list(input().split())
    
    if _str[0] == "push":
        result.append(int(_str[1]))
            
    elif _str[0] == "pop":
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop(0))
            
    elif _str[0] == "size":
        print(len(result))
        
    elif _str[0] == "empty":
        if len(result) == 0:
            print(1)
        else:
            print(0)
            
    elif _str[0] == "front":
        if len(result) == 0:
            print(-1)
        else:
            print(result[0])
    
    elif _str[0] == "back":
        if len(result) == 0:
            print(-1)  
        else:
            print(result[-1])
# 리스트를 사용하는 경우 임의의 위치 접근성이 뛰어나지만 맨 앞, 맨뒤는 느림
'''
import sys
from queue import Queue

def input():
    return sys.stdin.readline().strip()

N = int(input())
result = Queue()

for i in range(N):

    _str = list(input().split())
    
    if _str[0] == "push":
        result.put(_str[1])
            
    elif _str[0] == "pop":
        if result.qsize() == 0:
            print(-1)
        else:
            print(result.get())
            
    elif _str[0] == "size":
        print(result.qsize())
        
    elif _str[0] == "empty":
        if result.qsize() == 0:
            print(1)
        else:
            print(0)
            
    elif _str[0] == "front":
        if result.qsize() == 0:
            print(-1)
        else:
            print(result[0])
    
    elif _str[0] == "back":
        if result.qsize() == 0:
            print(-1)  
        else:
            print(result[-1])
            '''
'''            
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

queue = deque()
N = int(input())
for i in range(N):
    com = input().split()
    if com[0] == 'push':
        queue.append(com[1])
    elif com[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif com[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif com[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
            '''