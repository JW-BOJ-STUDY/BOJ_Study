from sys import stdin

input = stdin.readline

N = int(input().strip())

if N == 0:
    print("0") # 이게 왜 0인지는 조금 애매한거 같지만
elif N == 1:
    print("0")
else:
    current_num = 1
    for i in range(1,N+1):
        current_num *= i
    current_num = list(str(current_num))
    num_of_zero = 0
    while (current_num.pop() == '0'):
            num_of_zero += 1
    print(num_of_zero)

### 큰수를 계산한다 보면 런타임 에러가 발생할수 있음. 