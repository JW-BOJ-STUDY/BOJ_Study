def size():
    return len(Que)

def pushX(item):
    Que.append(item)

def pop():
    if size() > 0 : 
        return Que.pop(-1)
    else :
        return -1

def empty():
    if size() > 0 : 
        return 0
    else :
        return 1

def front():
    if size() > 0 : 
        return Que[0]
    else :
        return -1

def back():
    if size() > 0 : 
        return Que[-1]
    else :
        return -1
from sys import stdin

Que = []
num = int(stdin.readline())
for i in range(num):
    a = stdin.readline().split()
    
    if a[0] == 'push':
        pushX(a[1])
    elif a[0] == 'front':
        print(front())
    elif a[0] == 'back':
        print(back())
    elif a[0] == 'pop':
        print(pop())
    elif a[0] == 'size':
        print(size())
    elif a[0] == 'empty':
        print(empty())