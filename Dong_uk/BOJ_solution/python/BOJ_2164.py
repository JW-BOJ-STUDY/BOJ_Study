import sys

num = int(sys.stdin.readline())

cardList = [i+1 for i in range(num)]

while len(cardList) > 1:
    cardList.pop(0)
    a = cardList.pop(0)
    cardList.append(a)

print(cardList[0])




'''
from collections import deque
N = int(input())
deque = deque([i for i in range(1, N+1)])
while(len(deque) >1):
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)
        
print(deque[0])
'''
