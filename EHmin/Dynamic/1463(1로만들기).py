N = int(input())

result = 0 

while N != 1:
    if N % 3 == 0:
        N /= 3; result += 1
    elif N % 2 == 0:
        N /= 2; result += 1
    else:
        N -= 1; result += 1

def find_best(N):
    if N == 1:
        return 0
    if N % 3 == 0:
        return find_best(N/3) + 1
    if N % 2 == 0:
        return find_best(N/2) + 1
    if N != 1:
        return find_best(N-1) + 1
    print(1) # 
print(result)
