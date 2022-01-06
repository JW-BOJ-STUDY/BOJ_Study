# 18258,정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오
# 개빨리 짬 굳, 어제 다른 사람들 코드 리뷰 한 것도 짧게 짜는 데 도움이 되었따 ><

import sys
from collections import deque

N = int(sys.stdin.readline())
que = deque()

for i in range (N) :
    input_list = list(sys.stdin.readline().split())
    if input_list[0] == "push" :
        que.append(int(input_list[1]))
    elif input_list[0] == "pop" :
        print(-1) if len(que) == 0 else print(que.popleft())
    elif input_list[0] == "size" :
        print(len(que))
    elif input_list[0] == "empty" :
        print(1) if len(que) == 0 else print(0)
    elif input_list[0] == "front" :
        print(-1) if len(que) == 0 else print(que[0])
    elif input_list[0] == "back" :
        print(-1) if len(que) == 0 else print(que[-1])
    