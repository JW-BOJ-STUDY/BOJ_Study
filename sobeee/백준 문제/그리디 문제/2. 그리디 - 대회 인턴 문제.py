# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 23:10:49 2022

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline().strip()

N, M, K = map(int, input().split())

n = N//2 #여학생 그룹 수
match_group = 0 #대회 참가 그룹 최대 수
participate_group = 0 #인턴쉽 제외 대회 참가 그룹 수

if n > M:
    match_group = M
    rest_n = n - match_group
    participate_group = match_group
    K = K - rest_n*2

elif n < M:
    match_group = n
    rest_M = M - match_group
    participate_group = match_group
    K = K-rest_M

else:
    match_group = n
    participate_group = match_group


while(K > 0):
    K-=3
    participate_group-=1

print(participate_group)