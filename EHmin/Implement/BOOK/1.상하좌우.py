import sys

N =  int(sys.stdin.readline().strip())
move = sys.stdin.readline().split()

position = [1,1]

for i in move: #각각의 움직임에 따라
    if i == 'R':
        position[0] += 1
        if position[0] > N:
            position[0] = N
    elif i == 'L':
        position[0] -= 1
        if position[0] < 1:
            position[0] = 1
    elif i == 'U':
        position[1] -= 1
        if position[1] < 1:
            position[1] = 1
    elif i == 'D':
        position[1] += 1
        if position[1] > N:
            position[1] = N
            
sys.stdout.write(str(position[1]) +" "+ str(position[0]))

