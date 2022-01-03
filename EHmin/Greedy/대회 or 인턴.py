import sys

N,M,K = map(int, sys.stdin.readline().split())

teamCount = N//2

while (M < teamCount) or (N + M - K < 3*teamCount):
    teamCount -= 1
    
sys.stdout.write(str(teamCount))

# 4 3 1 >> 4 + 3 -1 < 3*2 