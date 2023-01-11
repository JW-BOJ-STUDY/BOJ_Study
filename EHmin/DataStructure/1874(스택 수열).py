from sys import stdin, stdout

input = stdin.readline

input_num = [i for i in range(int(input()),0,-1)]
myStack = []
result = []
is_possible = True

myStack.append(input_num.pop())
result.append("+")

for i in range(len(input_num) + 1):
    n = int(input())
    while(is_possible):
        if len(myStack) == 0:
            myStack.append(input_num.pop())
            result.append("+")
        elif myStack[-1] == n:
            myStack.pop()
            result.append("-")
            break
        elif myStack[-1] < n :
            myStack.append(input_num.pop())
            result.append("+")
        elif myStack[-1] > n:
            is_possible = False
            break
if is_possible:
    for word in result:
        print(word)
else:
    print("NO")
        