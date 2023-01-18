from sys import stdin
from collections import Counter

input = stdin.readline

n = int(input().strip())
sequence = list(map(int, input().split()))
f = dict(Counter(sequence))

my_stack = []
result = [-1] * n 
my_stack.append(0)
for i in range(1,n):
    while my_stack and f[sequence[my_stack[-1]]] < f[sequence[i]] :
        result[my_stack.pop()] = sequence[i]
    my_stack.append(i)

print(*result)

