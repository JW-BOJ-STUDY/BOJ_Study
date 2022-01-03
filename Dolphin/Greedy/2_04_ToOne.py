# 1이 될때까지
# 가능하면 나누는 것이 항상 더 숫자를 빠르게 줄이는 방법이 된다 
# 문제 풀이를 봐도.. 더 좋은 방법인지는 잘 모르겠다.. 숫자가 많아지면 느려지긴 할 듯.. 
import sys 

N, K = map(int, sys.stdin.readline().split())
count = 0

while(N>1) :
    if (N%K == 0) : N //= K
    else : N -= 1
    count += 1
    
print(count)