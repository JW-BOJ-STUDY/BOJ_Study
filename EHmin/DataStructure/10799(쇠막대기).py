from sys import stdin, stdout
input = stdin.readline
print = stdout.write

sentence = list(input().replace("()","1").strip())

scale = 0
result = 0
for word in sentence:
    if word == "(":
        scale = scale + 1
    elif word == "1":
        result = result + scale
    else:
        result = result + 1
        scale = scale - 1
        
print(str(result))
