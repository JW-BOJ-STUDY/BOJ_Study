import sys

N, K = map(int, sys.stdin.readline().split())
count = 0 

while True:
    if N == 1:
        break
    if N % K == 0:
        N = N / K
        count += 1
    else:
        N -= 1
        count += 1
        
sys.stdout.write(str(count) + "\n")