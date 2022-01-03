# 숫자 카드 게임 
# 각 행마다 가장 작은 수를 찾은 뒤에 그 수중에서 가장 큰수를 찾는 것
import sys 
N,M = map(int, sys.stdin.readline().split())
max_num = 0

for i in range(0,N) :
    nlist = list(map(int, sys.stdin.readline().split()))
    min_num = min(nlist)
    if max_num < min_num : max_num = min_num
    
print(max_num)

# nlist.sort()
# num = nlist[0]

# max_num = max(max_num, min_num)
# 와 위에거는 신박하다... 
    