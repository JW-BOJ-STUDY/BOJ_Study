# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys

def input():
    return sys.stdin.readline()

N, M, K = map(int, input().split())

#array = map(int,input().split()) 오답
array = list(map(int,input().split())) #리스트로 만들어주기
big = 0
second = 0

for i in range(N):
    if big < array[i]:
        second = big
        big = array[i]

#방법 2번째
#array.sort()
#first = data[n-1]
#second = data[n-2]


#big이 K번, second가 1번 -> K+1번이 세트
#이걸 M번 과 나머지연산을 사용해서 세트 반복수 계산 

big_set = (big*K) + second

result = 0
result = (big_set * (M // (K+1))) + ((M % (K+1)) * big) #더하기 연산은 우선순위 낮으므로 괄호 관리 잘하기

print(result)