# 2164, N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.
# 이것도 10분이면 하는 듯.. 
# While True로 그대로 두고 할 수 있는 방법이 있었다..!
import sys
from collections import deque

N = int(sys.stdin.readline())
que = deque(i for i in range(1, N+1))

while len(que)!=1 : 
    que.popleft()
    if len(que)!=1 : que.append(que.popleft())
    else : break
print(que.pop())


''' 아래 코드가 훨씬 빠르고 간결하다
while True : 
    a = que.popleft()
    if len(que) == 0 : 
        print(a)
        break
    else : que.append(que.popleft())
'''