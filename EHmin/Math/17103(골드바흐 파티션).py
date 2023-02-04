import math 
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

def is_prime_number(a):
    if a == 1: # 1에대한 예외 처리를 잊지 말고 해주어야 한다
        return False
    for i in range(2,int(math.sqrt(a))+1): #루트 N 이상의 경우는 확인할 필요가 없다
        if (a % i) == 0:
            return False
    return True

prime_list = []
for i in range(1000000):
    if is_prime_number(i):
        prime_list.append(i)

for _ in range(int(input().strip())):
    N = int(input().strip())
    result = 0
    for i in range(3, int(N/2) + 1, 2):
        a = i
        b = N - i 
        if is_prime_number(a) and is_prime_number(b):
            result += 1
    print(str(result) + "\n")