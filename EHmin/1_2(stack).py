# class stack:
    
#     def __init__(self):
#         self.list = []
        
#     def push(self, x):
#         self.list.append(x)
    
#     def pop(self):
#         if len(self.list) == 0:
#             return -1
#         else:
#             return self.list.pop()
        
#     def size(self):
#         return len(self.list)
    
#     def empty(self):
#         if len(self.list) == 0: return 1
#         else: return 0
        
#     def top(self):
#         if len(self.list) == 0:
#             return -1 
#         else:
#             x = self.list.pop()
#             self.list.append(x)
#             return x

## input 쓰면 느려서 안돌아간다. ㅎ 

import sys

N = int(sys.stdin.readline())

myStack = []

for i in range(N):
    arr = sys.stdin.readline().strip()
    if " " in arr:
        arr , x = arr.split()
        myStack.append(int(x))
        
    elif arr == "pop":
        if len(myStack) == 0:
            print(-1)
        else:
            print(myStack.pop())
        
    elif arr == "size":
        print(len(myStack))
        
    elif arr == "empty":
        if len(myStack) == 0: print(1)
        else: print(0)
    
        
    elif arr == "top":
        if len(myStack) == 0:
            print(-1) 
        else:
            x = myStack.pop()
            myStack.append(x)
            print(x)
            