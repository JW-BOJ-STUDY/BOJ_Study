from sys import stdin, stdout

input = stdin.readline
print = stdout.write

MyStack = []

for _ in range(int(input())):
    WordList = list(input())
    for word in WordList:
        if word == "(":
            MyStack.append("(")
        elif word == ")":
            if len(MyStack) == 0:
                MyStack.append(")")
                break
            else:
                MyStack.pop()
                
    if len(MyStack) == 0:
        print("YES\n")
    else:
        print("NO\n")
    MyStack.clear()