from sys import stdin, stdout

input = stdin.readline

n = int(input().strip())

sentence = list(input().strip())
my_stack = []

for i in range(n):
    if sentence[i].isupper():
        my_stack.append(sentence[i])
        print(my_stack)
    else:
        a = my_stack.pop()
        b = my_stack.pop()
        ex = "".join[a,sentence[i],b]
        my_stack.append(eval(a,str(sentence[i]),b))

print(my_stack)