# from sys import stdin, stdout
# input = stdin.readline

# _ = input().strip()

# word = list(input().strip())

# my_stack = []
# temp_str = [] 

# alphabet = ""
# temp_number = 0.0
# expression = ""

# for word in word:
#     if word.isupper():
#         if alphabet == word:
#             _
#         else:
#             temp_number = float(input().strip())
#             alphabet = word
#         my_stack.append(temp_number)
#     else:
#         temp_str.clear()
#         temp_str.append(str(my_stack.pop()))
#         temp_str.append(word)
#         temp_str.append(str(my_stack.pop()))
#         expression = ""
#         expression = "".join(temp_str[::-1])
#         my_stack.append(float(eval(expression)))
        
# answer = float(my_stack.pop())
# print("{:.2f}".format(answer)) 
#########################################################################
#위의 코드의 경우 런타임 에러 발생. 
# 세가지 가능성 존재
# 1.eval() 함수에서 알지 못하는 동작. >> 완벽하게 동작을 이해한 함수만 사용
# 2.결과를 문자열로 저장해서 발생하는 문제. >> 의도에 맞는 형식으로 저장합시다. 
# 3.index 접근 방식의 차이. 위의 코드의 경우 첫 input을 이용하지 않음. 최대한 문제의 흐름대로 수행하려는 노력이 필요ㄴ
from sys import stdin, stdout

input = stdin.readline

N = int(input().strip())

posterior_notation = list(input().strip())

operand = []
for _ in range(N):
    operand.append(int(input().strip()))
    
my_stack = []
temp_left = 0
temp_right = 0

for word in posterior_notation:
    if word.isupper():
        my_stack.append(operand[ord(word) - 65])
    else:
        temp_right = my_stack.pop()
        temp_left = my_stack.pop()
        if word == "+":
            my_stack.append(temp_left + temp_right)    
        elif word == "-":
            my_stack.append(temp_left - temp_right)    
        elif word == "*":
            my_stack.append(temp_left * temp_right)    
        elif word == "/":
            my_stack.append(temp_left / temp_right)    
            
answer = float(my_stack.pop())
print("{:.2f}".format(answer)) 

        