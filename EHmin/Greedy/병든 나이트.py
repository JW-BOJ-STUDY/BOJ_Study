import sys

N, M  = map(int, sys.stdin.readline().split())

count = 1

if N == 1 or M == 1:
    count = count
elif N == 2:
    count += (M - 1)//2
    if(count > 4):
        count = 4
else:
    if M < 7:
        count += (M - 1)
        if(count > 4):
            count = 4
    else:
        count += (M - 5) + 2
        
sys.stdout.write(str(count) + "\n")