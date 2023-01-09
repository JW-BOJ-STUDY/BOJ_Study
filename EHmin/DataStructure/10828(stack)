from sys import stdin, stdout

input = stdin.readline

N = input()
stack = []

def push(x):
    stack.append(x)
    
def pop():
    if len(stack) == 0:
        print("-1")
    else:
        print(str(stack.pop()))

def size():
    print(str(len(stack)))

def empty():
    if len(stack) == 0:
        print("1")
    else:
        print("0")

def top():
    if len(stack) == 0:
        print(str(-1))
    else:
        x = stack.pop()
        stack.append(x)
        print(str(x))


for i in range(int(N)):
    input_list = input().split()
    if input_list[0] == "push":
        push(input_list[1])
    elif input_list[0] == "pop":
        pop()
    elif input_list[0] == "size":
        size()
    elif input_list[0] == "empty":
        empty()
    else:
        top()
    
    


