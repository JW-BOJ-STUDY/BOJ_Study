# 예제 3-1, 거스름돈 
# 500, 100, 50, 10 무제한 
# 거슬러줘야 할 돈 N원, N의 최소 개수, N은 항상 10의 배수
import sys

N = int(sys.stdin.readline())
changelist = [500, 100, 50, 10]

for i in range(len(changelist)) :
    coin = changelist[i]
    changelist[i] = N // coin
    N %= coin

print(changelist)
