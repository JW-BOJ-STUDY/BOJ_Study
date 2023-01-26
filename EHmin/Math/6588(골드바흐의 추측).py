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

while True:
    N = int(input().strip())
    if N == 0:
        break
    for i in range(3,N,2):
        a = i
        b = N - i 
        if is_prime_number(a) and is_prime_number(b):
            print(str(N) + " = " + str(a) +" + " + str(b))
            break
        elif i == (N-10):
            print("Goldbach's conjecture is wrong")
            
# 문제가 합리적이지는 못한것 같다... 최악의경우 시간복잡도를 초과할 가능성이 있음!
# 다만 해당하는 최악의 경우를 찾는것도 너무 어려움!
    
        