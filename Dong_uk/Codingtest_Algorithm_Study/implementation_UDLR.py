#구현 시간 복잡도 널널 o(N)의로 구현 

import sys

N = int(sys.stdin.readline())
plan = list(sys.stdin.readline().split())

locationX = 0 
locationY = 0 

for move in plan:
    if move == 'R':
        if locationX != N:
            locationX +=1
    elif move == 'L':
        if locationX != 0:
            locationX -=1
    elif move == 'U':
        if locationY != 0:
            locationY -=1
    elif move == 'D':
        if locationY != N:
            locationY +=1

print(locationX,locationY)