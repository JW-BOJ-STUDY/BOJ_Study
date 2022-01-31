# 한시간에 3이 들어가는 시간들
import sys 

N = int(sys.stdin.readline())

count = 0

for i in range(N+1):
    if i%3 == 0 : 
        count += 1
    for ii in range(0,60):
        for iii in range(0,60):
           if '3' in str(i)+str(ii)+str(iii): #숫자를 문자로 만들어 쉽게 유무를 찾을 수있다.
               count += 1

print(count)