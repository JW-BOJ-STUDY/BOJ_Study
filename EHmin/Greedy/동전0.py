import sys

N,K = map(int, sys.stdin.readline().split())

coins = [int(sys.stdin.readline().strip()) for _ in range(N)]

count = 0

for i in range(N):
    if(K==0):
        break
    count += K//coins[N-i-1]
    K = K - coins[N-i-1] * (K//coins[N-i-1])
    
sys.stdout.write(str(count) + "\n")