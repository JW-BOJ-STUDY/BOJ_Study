import sys

position = list(sys.stdin.readline().strip()) #list()의 정확한 작동원리를 모르겠다. 나중에 확인해보자.

position[0] = ord(position[0]) - 96 #아스키 코드를 이용해서 숫자로 변환. 
position[1] = int(position[1])

possiblePosition = [] #8가지 경우의 수를 저장

possiblePosition.append([position[0]+1, position[1]-2])
possiblePosition.append([position[0]+2, position[1]-1])
possiblePosition.append([position[0]+2, position[1]+1])
possiblePosition.append([position[0]+1, position[1]+2])
possiblePosition.append([position[0]-1, position[1]+2])
possiblePosition.append([position[0]-2, position[1]+1])
possiblePosition.append([position[0]-2, position[1]-1])
possiblePosition.append([position[0]-1, position[1]-2])

output = 0

for pos in possiblePosition:
    if pos[0] <1 or pos[0] > 8 or  pos[1] <1 or pos[1] > 8: #모든 경우의 수중, 체스판을 벗어나는 경우를 제외하고 가능한 경우를 계산
        continue
    output += 1
    
print(output)