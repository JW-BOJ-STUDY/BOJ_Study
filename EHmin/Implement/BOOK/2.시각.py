import sys

N = int(sys.stdin.readline().strip())

output = 0 

three = '3'
## 항상 range의 마지막 부분이 안들어가는 것에 유의 하자. 횟수를 계산할 때는 상관없지만, 정확한 숫자를 돌리는 경우 조심할것
for hour in range(N + 1):
    for i in range(60):
        for j in range(60):
            if three in str(hour) + str(i) + str(j):
                output += 1
            
print(output)
    