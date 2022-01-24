#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 14:58:54 2022
@author: baehongseob
"""

import sys

def input():
    return sys.stdin.readline().strip()

#2칸 위로 1칸 오른쪽
#1칸 위로 2칸 오른쪽
#1칸 아래, 2칸 오른쪽
#2칸 아래, 1칸 오른쪽 --> 무조건 오른쪽으로 1칸은 가

n, m = map(int,input().split())

#체스판의 크기 세로n 가로 m
#방문할 수 있는 칸의 최대 개수
#이때 무조건 오른쪽으로 움직이니까 가장 많이 이동 -> 절대 겹칠 수 없음

#따라서 위아래 반복하면서 오른쪽 1칸씩만 움직여야 최대

#1초 1억 - 3억 따라서 2억 - 6억인데 20억이니까 O(logn)

#n도 고민을 해

count = 0

if n == 1: #이동 불가
    count = 1
elif n == 2: # -> 오른쪽으로 2칸씩만 이동 가능
    #이동횟수 4회이상 고려해줘야함 이거 안해서 틀림
    if m >= 9: #이동횟수 4회이상이면 4가지 이동방법 모두 사용해야하는데 위로 2칸은 가지못해서 불가능
        count = 4
    else: #이동횟수 4회 미만
        if (m % 2) == 0: # m이 짝수
            count = m // 2
        else: # m이 홀수
            count = 1 + (m//2)
else: # n이 3이상
    if m <= 3: #이동횟수 4회 미만 중 1칸씩만 이동
        count = m
    elif m == 4 or m == 5: #이동횟수 4회이상은 4가지 이동방법 모두 사용해야하므로 m이 6이상이여야한다.
    #따라서 4(2,1,1) 5(2,2,1) 이렇게 고정.
        count = 4
    elif m >= 6: #이동횟수 4회 이상
        count = 4 + m-6 #이동방법 4가지 사용 & 오른쪽 1칸씩만 이동하여 최대 방문
        
print(count)