# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 13:22:56 2022

@author: bhs89
"""

import sys
from operator import itemgetter #다차원 배열 정렬 


def input():
    return sys.stdin.readline().strip()

N = int(input())
meeting_list = []

for i in range(N):
    start, end = map(int, input().split())
    meeting_list.append([start,end])

meeting_list.sort(key=itemgetter(1,0)) #itemgetter parameter = 다차원 배열에서 정렬 기준 index
#meeting_list.sort(key = lambda x: (x[1], x[0]))

end_time = meeting_list[0][1] # 맨 처음 회의 끝나는 시간 대입
count = 1

for i in range(1,N):
    if end_time <= meeting_list[i][0]: # root(이전 회의 끝나는시간) 과 다음회의 시작시간을 비교
        count += 1
        end_time = meeting_list[i][1] # 끝나는 시간 수정
        
print(count)


'''답지
import heapq
import sys
input = sys.stdin.readline


N = int(input())
queue = []
for _ in range(N):
    a, b = map(int, input().split())
    heapq.heappush(queue, (b, a))

end = 0
cnt = 0
for _ in range(N):
    b, a = heapq.heappop(queue)
    if a >= end:
        cnt += 1
        end = b
        
print(cnt)
'''

'''[응용] 최대 힙, 우선순위 큐
heapq모듈은 기본이 min heap인데, max heap을 구하려면 튜플(tuple)을 이용하면 된다.
이렇게 우선순위를 정하여 구할 수 있다.

num = [5, 3, 4, 2, 1]
heap = []

for n in num:
    heapq.heappush(heap, (-n, n))  # (우선순위, 값)

# 우선순위와 함께 출력
while heap:
    print(heapq.heappop(heap))

"""
(-5, 5)
(-4, 4)
(-3, 3)
(-2, 2)
(-1, 1)
"""
'''
