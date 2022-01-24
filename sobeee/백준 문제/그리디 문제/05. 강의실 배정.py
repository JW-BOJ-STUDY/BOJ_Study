# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 21:44:17 2022

@author: bhs89
"""
'''

import sys

def input():
    return sys.stdin.readline().split()

N = int(input()) #N개의 수업
S = []
T = []
walk_s = 0 # S[i] 좌표
walk_t = 0 # T[i] 좌표
num_classroom = 0 #전체 강의실 수
count = 0 #현재 진행에서 필요한 강의실 수

for i in range(N):
    s, t = map(int, input())
    S.append(s)
    T.append(t)
    
while(True):
    if T[walk_t] > S[walk_s]:
        count += 1
        walk_s += 1
    else:
        walk_t = walk_s + 1
'''

# 강의실 수를 max로 해놓고 합치면서 1씩 줄여가는 방법
# 시간복잡도 너무 오래걸릴 것 같은데
# 조금 더 고민해보자

'''
heap 구조 사용하기
heap 구조란? 
1. parent node가 <= child node (L.child와 R.child 구분 x) 따라서 root node가 최소값
2. height가 최소일 것 -> 왼쪽부터 꽉꽉 채운 tree구조

python에서 heapq라는 라이브러리로 제공한다.
add -> heappush     마지막 leaf에 추가 후 upheap를 height만큼 반복
remove -> heappop   root node와 last leaf node를 교체, 이후 downheap 를 height만큼 반복
ex) heapq.heappush(array, value)
    heapq.heappop(array)

결론 -> 추가, 제거가 o(logn) 이다.

시간복잡도가 o(logn)이 필요할 경우 node를 사용한 구조를 고민할 것
'''

import sys
import heapq

def input():
    return sys.stdin.readline().strip()

N = int(input())
array_list = []

for i in range(N):
    S, T = map(int, input().split())
    array_list.append([S, T])
    
array_list.sort()

'''
arr = [[2,3], [1,2], [0,4]]
arr.sort()
print(arr)
#[[]]

arr.sort(key=lambda x:x[0]) #행 기준 오름차순 axis라고 생각
print(arr)

arr.sort(key=lambda x:-x[0]) #행 기준 내림차순
print(arr)

arr.sort(key=lambda x:x[1]) #열 기준 오름차순
print(arr)

arr.sort(key=lambda x:-x[1]) #열 기준 내림차순
print(arr)

arr.sort(key=lambda x:(x[1], x[0])) # 열 값이 같을 경우 행 내림차순 정렬
'''

num_room = []
heapq.heappush(num_room,array_list[0][1]) # column 1이 끝나는 시간

for i in range(1,N):
    if num_room[0] > array_list[i][0]: # array_list[i][0] column 0 이 시작시간 주의
        heapq.heappush(num_room, array_list[i][1]) # 추가는 column 1 (끝나는 시간)
    else:
        heapq.heappop(num_room)
        heapq.heappush(num_room, array_list[i][1])

print(len(num_room))
