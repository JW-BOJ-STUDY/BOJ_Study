from sys import stdin 
input = stdin.readline

def is_prime_number(a):
    if a == 1: # 1에대한 예외 처리를 잊지 말고 해주어야 한다. 
        return 0
    for i in range(2,a):
        if (a % i) == 0:
            return 0
    return 1
        
N = int(input().strip())
int_list = list(map(int, input().split()))

result = 0

for number in int_list:
    result += is_prime_number(number)
    
print(result)
