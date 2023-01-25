from sys import stdin
import math
input = stdin.readline

def GCD(a,b):
    max_ab = max(a,b)
    min_ab = min(a,b)
    while min_ab != 0:
        temp = max_ab % min_ab
        max_ab = min_ab
        min_ab = temp
    return max_ab
#유클리드 호제법을 사용하지 않는경우 시간 초과가 발생하게 된다. 



for _ in range(int(input())):
    N, *test_case = map(int, input().split())
    result = 0 
    for i in range(N):
        for j in range(i+1,N):
            # result += math.gcd(test_case[i], test_case[j])
            # math.gcd는 유클리드 호제법을 이용해서 좀더 빠르게 계산하는것으로 추정.
            result += GCD(test_case[i], test_case[j])
    print(result)
    
