from sys import stdin 
import math
input = stdin.readline

def is_prime_number(a):
    if a == 1: # 1에대한 예외 처리를 잊지 말고 해주어야 한다. 
        return False
    for i in range(2,int(math.sqrt(a))+1): #루트 N 이상의 경우는 확인할 필요가 없다. 
        if (a % i) == 0:
            return False
    return True

a, b = map(int,input().split())

for number in range(a,b+1):
    if is_prime_number(number):
        print(number)