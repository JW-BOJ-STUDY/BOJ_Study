# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 22:11:08 2022

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline().strip()

# checkRoad를 통해 길을 건널 수 있는가 판단
# 이때 list 와 reverselist를 보내어 둘다 True일때 길을 건널 수 있다고 판단
# 경사로가 올라갈 수 있지만 내려갈 수 도 있으므로 두 조건 모두 만족해야한다.


'''
한쪽 검사하고 reverse로 검사할 경우
2 1 1 2 구조에서 True로 인식한다.
이 구조는 안되므로 예외발생
'''
def checkRoad(oneway,L):
    # oneway 길이는 N
    N = len(oneway)
    avail = 1 #다리를 놓을 수 있는 칸 개수 default 값 1
    
    for i in range(N-1):
        interval = oneway[i+1] - oneway[i] #i는 index -> N-1미만. N-2까지만
        
        # 높이가 같은 경우 그냥 진행
        if interval == 0:
            avail += 1
        # 경사로를 놓을 수 있는 경우는 interval == 1 or -1
        elif interval == 1:
            # 경사로를 놓을 수 없음
            if avail < L:
                return False
            # 경사로를 놓을 수 있음 -> avail 초기화
            else:
                avail = 1      
        # 올라가는거만 계산함. 내려가는건 보류
        elif interval == -1:
            avail = 1
            continue 
        # interval이 -1, 0 ,1 이 아닌경우 경사로 놓을 수 없음
        else:
            return False
        
    #반복문을 성공적으로 탈출한 경우
    return True

N, L = map(int, input().split())
count = 0 #가능한 길의 개수
_square = []

# 입력과 동시에 가로 길 건널 수 있는지 확인
for i in range(N):
    row = list(map(int, input().split()))
    _square.append(row)
    a = checkRoad(row,L)
    if a == True:
        reverse_row = reversed(row)
        b = checkRoad(reverse_row,L)
        if b == True:
            count+=1
        
for i in range(N):
    # i가 바뀔때마다 column 초기화
    column = []
    
    #column list 완성
    for j in range(N):
        column.append(_square[j][i])
    a = checkRoad(column,L)
    if a == True:
        column.reverse()
        b = checkRoad(column, L)
        if b == True:
            count+=1

print(count)