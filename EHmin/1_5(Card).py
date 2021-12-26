import sys
from collections import deque

N = int(sys.stdin.readline().strip())

cards = deque()

for i in range(N):
    cards.append(i+1)

while True:
    x = cards.popleft()
    if len(cards) == 1 :
        print(cards.pop())
        break
    elif len(cards) == 0:
        print(x)
        break
    x = cards.popleft()
    cards.append(x) 
    

    