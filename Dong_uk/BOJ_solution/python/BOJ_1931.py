from re import M
import sys 

N = int(sys.stdin.readline())
list = [[0]*2 for i in range(N)]

for i in range(N):
    n,m = map(int,sys.stdin.readline().split())
    list[i][0] = n
    list[i][1] = m

list.sort()
