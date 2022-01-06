import sys

N,M,K = map(int, sys.stdin.readline().split())

teamCount = N//2

while (M < teamCount) or (N + M - K < 3*teamCount):
    teamCount -= 1
    
sys.stdout.write(str(teamCount))
