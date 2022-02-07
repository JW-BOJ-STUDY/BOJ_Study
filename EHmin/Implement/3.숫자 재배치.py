from itertools import permutations
import sys

A, B = sys.stdin.readline().split()

a = list(A) #a문자열을 리스트로 변환
b = list(B)

permutations = list(permutations((a), len(a)))

permutations.sort(reverse=True)

output = 0 

for num in permutations:
    if int(''.join(num)) < int(''.join(b)) and num[0] != '0':
        output = int(''.join(num))
        break;

if output == 0:
    sys.stdout.write("-1")
else:
    sys.stdout.write(str(output))
    






### 아래 코드로 하면, 현재 상태만 확인이 가능, 즉 2345 5043이 주어지면, 일단 가장앞에 5를 가져오는데 그러면 항상 커지게 됨.
# 그럼 다시 뒤로 돌아가서 맨 앞에 숫자를 바꾸어 주어야 하는데 이런것이 아래 코드로 만들기에는 너무 어렵다. 
# fullLengthofA = len(a)

# a.sort(reverse=True)

# output = []

# def makeBiggest(index):
#     index += 1 
#     for i in range(len(a)):
#         if int(a[i]) == int(b[index]):
#             output.append(a.pop(i))
#             makeBiggest(index)
#             break
#         elif int(a[i]) < int(b[index]):
#             output.append(a.pop(i))
#             output.extend(a)
#             break

# if len(a) < len(b):
#     output.extend(a)
# elif len(a) > len(b):
#     output.append('0')
# else:
#     makeBiggest(-1)

# if len(output) == 0:
#     output.append('0')
        

# if output[0] == '0' or int("".join(output)) >= int("".join(b)) or len(output) != fullLengthofA :
#     sys.stdout.write(str(-1))
# else:
#     sys.stdout.write(str("".join(output)))
