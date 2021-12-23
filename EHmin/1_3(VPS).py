import sys

class stack():
    def __init__(self):
        self.list = []
        
    def pop(self):
        if len(self.list) == 0:
            return -1
        else:
            return self.list.pop()
        
    def push(self, x):
        self.list.append(x)
        
    def size(self):
        return len(self.list)
        
        
def isVPN(arr):
    #arr = sys.stdin.readline().split()
    myStack = stack()
    for word in arr:
        if word == "(":
            myStack.push(word)
        else:
            if myStack.pop() == -1:
                return "NO"
    if myStack.size() == 0:
        return "YES"
    else: 
        return "NO"

N = int(sys.stdin.readline().strip())

for i in range(N):
    print(isVPN(sys.stdin.readline().strip()))