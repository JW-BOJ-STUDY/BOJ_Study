#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 22:44:56 2022

@author: baehongseob
"""


N = '125'
num_broken_button = 1
if num_broken_button != 0:
    list_broken_button = [1,2,3,4,5,6,8,9]
else:
    list_broken_button = [10]
print(list_broken_button)
# not in 가능!
available_button = [i for i in range(10) if i not in list_broken_button]
print(available_button)
#다 차원 배열? 아니면 window 처럼?

# N을 각 자릿수 숫자 배열로 변환 5457이면 5,4,5,7
N_list = []
for i in N:
    N_list.append(int(i))


example = [[0 for i in available_button] for j in N_list]

i=0 #자릿수 의미
num = ''
# 0에 가깝게 정렬? -> 절댓값 사용하면 되지
for n_list in N_list: # 최대 6번
    j=0
    if n_list in available_button:
        num += str(n_list)
        i+=1
        continue
    # 이쪽에서 num을 확정할꺼라 i증가 안시켜줘도 됨
    else:
        for avail in available_button: # 최대 10번
            example[i][j] = abs(n_list - avail)
            j+=1
        break

            
if i == len(N):
    count = len(N)
# 리모컨 버튼 사용이 안될 경우
elif len(available_button) == 0:
    count = abs(int(N)-100)
# 리모컨 버튼이 0 밖에 안될 경우
elif len(available_button) == 1 and available_button[0] == 0:
    #0으로 이동 후 +버튼만 클릭
    count = int(N)+1
else:
    first_min = min(example[i])
    num1 = num+str(available_button[example[i].index(first_min)])
    
    interval = int(N[i]) - available_button[example[i].index(first_min)]
    plus_interval = int(N[i]) + interval
    if interval > 0:
        #num1 은 N보다 작은 수 중 가장 가까운 수
        for i in range(len(N)-len(num1)):
            num1 += str(max(available_button))
        print(num1)
        #num2 는 N보다 큰 수 중 가장 가까운 수
        if plus_interval < 10:
            num2 = num+ str(plus_interval)
            for i in range(len(N)-len(num2)):
                num2 += str(min(available_button))
            count = min(int(N) - int(num1), int(num2) - int(N))
        else:
            count = int(N) - int(num1)
        print(num2)
        print(count)
        # N 과 num1, num2 차이 구하면 됨.
        count += len(num1)
    # num1이 N보다 큰 경우
    else:
        for i in range(len(N)-len(num1)):
            num1 += str(min(available_button))
        count = int(num1) - int(N)
        count += len(num1)
        
gap_N = abs(int(N) - 100)  
count = min(count, gap_N)         
print(count)