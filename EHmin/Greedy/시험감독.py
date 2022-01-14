import sys

N = int(sys.stdin.readline().strip())
stdInRoom = list(map(int, sys.stdin.readline().split()))
B,C = list(map(int, sys.stdin.readline().split()))

CNum = 0 

for item in stdInRoom:
    if( item <= B):
        continue
    elif((item - B)%C == 0):
        CNum += (item - B)//C
    else:
        CNum += (item - B)//C + 1
    
print(CNum + N)



