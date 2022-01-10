# 어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다. 
# 미르코는 30이란 수를 존경하기 때문에, 그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.
# 미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.

import sys

def input():
    return sys.stdin.readline().rstrip()

n = list(input())
n.sort(reverse=True)
sum_n=0

for word in n:
    sum_n += int(word)

if sum_n %3 != 0 or "0" not in n:
    print(-1)

else:
    print(''.join(n))
