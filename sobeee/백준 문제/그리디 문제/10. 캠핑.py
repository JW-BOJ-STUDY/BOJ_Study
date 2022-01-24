# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 13:37:42 2022

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline().strip()

i = 0 #Case i번째
while(True):
    L, P, V = map(int, input().split())
    
    if (L+P+V == 0):
        break
    else:
        i+=1
        # 조건 1 < L < P < V
        if (V % P) < L: #남은 날 모두 캠핑을 즐기는 경우      
            available_use_day = ((V // P)*L) + (V % P)
        else: #남은 날이 캠핑 가능한 날보다 많은 경우
            available_use_day = ((V // P)*L) + L
        
        #print("Case",i,':',available_use_day)
        print("Case %d: %d" %(i,available_use_day))