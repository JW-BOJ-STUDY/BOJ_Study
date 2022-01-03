# 큰 수의 법칙 
import sys 
sum = 0
count = 0

N, M, K = map(int,sys.stdin.readline().split())
nlist = list(sys.stdin.readline().split())
nlist.sort()
max_num = int(nlist[-1])
sec_num = int(nlist[-2])

for i in range(0,M) :
    if (count == K-1) :
        sum += sec_num
        count = 0
    else :  
        sum += max_num
        count += 1

print(sum)
    
# 와..따봉
# sum += max_num * (M/(K+1)*K) + sec_num * (M/(K+1))
# sum += max_num * (M%(K+1))
