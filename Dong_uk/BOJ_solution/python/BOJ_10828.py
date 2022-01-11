def size():
    return len(top)

def push(item):
    top.append(item)

def pop():
    if size() > 0 : 
        return top.pop(-1)
    else :
        return -1

def empty():
    if size() > 0 : 
        return 0
    else :
        return 1

def top2():
    if size() > 0 : 
        return top[-1]
    else :
        return -1

top = []
out = []
num =  int(input())
for i in range(num):
    a = input().split()
    
    if a[0] == 'push':
        push(a[1])
    elif a[0] == 'top':
        out.append(top2())
    elif a[0] == 'pop':
        out.append(pop())
    elif a[0] == 'size':
        out.append(size())
    elif a[0] == 'empty':
        out.append(empty())
        
for i in range(len(out)):
    print(out[i])