# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 16:04:09 2022

@author: bhs89
"""

import sys
from operator import itemgetter #다차원 배열 정렬 

def input():
    return sys.stdin.readline().strip()

N = int(input())

number_of_people = [i for i in range(N)]

time_list = list(map(int, input().split())) #list로 감싸는거 기억하기
#split() 괄호 빼먹었었음..
pair_of_people_and_time = []

for i in range(N):
    pair_of_people_and_time.append([number_of_people[i], time_list[i]])

pair_of_people_and_time.sort(key=itemgetter(1,0)) # 걸리는시간이 짧은 순으로 정렬

#take_time list 계산
take_time = [pair_of_people_and_time[0][1]]
for i in range(1,N):
    take_time.append(take_time[i-1] + pair_of_people_and_time[i][1])

#총 걸리는 시간 계산
sum_of_time = 0
for i in range(N):
    sum_of_time += take_time[i]

print(sum_of_time)


'''답지 -> 개쉬움 사람이람 왜 엮음? 시간만 알면되는데 사람순서는 필요없음
n = int(input()) # 사람 수 
arr = list(map(int,input().split())) # 인출 시간
arr.sort() # 정렬

result = 0

for i in range(1,n):
    arr[i] += arr[i-1] # 인출 시간 갱신

print(sum(arr))
'''

'''욱쓰
import sys

N = int(input())

number_of_people = [i for i in range(N)]

time_list = list(map(int, sys.stdin.readline().split()))  # list로 감싸는거 기억하기
time_list.sort()

#누적합 표현 이게 미친듯
pair_of_people_and_time = [sum(time_list[: i + 1]) for i in range(len(time_list))]

print(sum(pair_of_people_and_time))
'''
