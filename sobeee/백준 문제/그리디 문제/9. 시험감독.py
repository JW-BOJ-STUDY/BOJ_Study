# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 13:00:23 2022

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline().strip()

N = int(input())

num_of_playground = list(map(int, input().split()))

B, C = map(int, input().split())

supervisor = 0

for i in num_of_playground:
    if i <= B: #총 감독관만 필요한 경우
        supervisor += 1
    else: #부 감독관까지 필요한 경우
        student = i-B #총 감독관 감독 학생수
        supervisor += 1 + ((student-1)//C) +1 #뒤에 if문을 줄일 수 있음 왜?
'''        if (student % C) == 0:
            supervisor += 1 + (student // C)
        else:
            supervisor += 1 + ((student // C) + 1) #앞에 1은 총 감독관, 뒤에는 남은 학생들을 부감독관수로 나눈 몫
            #if C(부감독관 학생수)가 3이고 학생수가 8이라면 3명의 부감독이 필요하다.
'''
print(supervisor)