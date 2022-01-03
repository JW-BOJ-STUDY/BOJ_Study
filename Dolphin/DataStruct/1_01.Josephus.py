# 1158, N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
from collections import deque

N, K = map(int, input().split())

que = deque([i for i in range (1, N+1)])
plist = []

while (que) :
    for k in range(0,K-1) :
        que.append(que.popleft())
    plist.append(que.popleft())
    if (len(que) == 1) : plist.append(que.popleft())

print("<" + str(plist)[1:-1] + ">")