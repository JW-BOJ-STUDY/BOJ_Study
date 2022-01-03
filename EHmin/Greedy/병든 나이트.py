import sys

N, M  = map(int, sys.stdin.readline().split())

count = 1

if N == 1 or M == 1:
    count = count
elif N == 2:
    count += (M - 1)//2
    