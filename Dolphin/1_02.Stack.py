# 10828, 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오
# 와... sys 하나로 바꿨다고 바로 시간통과...레전드
# Stack class 다시 구현해야 할 것 같음..

import sys
from collections import deque

class Stack() : 
    def __init__(self) : 
        self.stack = deque()
    def push(self, num) :
        self.stack.append(int(num))
    def pop(self) :
        if (len(self.stack) == 0) : print(-1)
        else :                      print(self.stack.pop())
    def size(self) :
        return print(len(self.stack))
    def empty(self) : 
        if (len(self.stack) == 0) : print(1)
        else :                      print(0)
    def top(self) :
        if (len(self.stack) == 0) : print(-1)
        else :                      print(self.stack[-1])
    def switch(self, key) :
        if key == "pop" : stack.pop()
        elif key == "size" : stack.size()
        elif key == "empty" : stack.empty()
        elif key == "top" : stack.top()
        
        
N = int(sys.stdin.readline())
input_list = []
stack = Stack()

for i in range (0, N) :
    input_list = sys.stdin.readline().split()
    if input_list[0]=="push" :
        stack.push(input_list[1])
    else :
        stack.switch(input_list[0])

    