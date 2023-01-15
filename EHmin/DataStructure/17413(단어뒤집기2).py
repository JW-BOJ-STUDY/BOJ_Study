from sys import stdin, stdout
input = stdin.readline
print = stdout.write

stack_for_word = []
result = []
is_word = True

str = list(input().strip())
for word in str:
    if word == "<":
        is_word = False
        for _ in range(len(stack_for_word)):
            result.append(stack_for_word.pop())
    if is_word == False:
        result.append(word)
        if word == ">":
            is_word = True
    else:
        if word == " ":
            for _ in range(len(stack_for_word)):
                result.append(stack_for_word.pop())
            result.append(word)
        else:
            stack_for_word.append(word)
            
for _ in range(len(stack_for_word)):
    result.append(stack_for_word.pop())
            
for i in result:
    print(i)

