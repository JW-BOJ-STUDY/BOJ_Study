import sys

N, M, K = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))

output = 0
preIndex = -1
index = 0
check = 0
    
for i in range(M):
    maximum = 0
    
    for j in range(N):
        if array[j] >= maximum:
            maximum = array[j]
            index = j 
        
    if preIndex == index:
            check += 1
    else:
        preIndex = index
        check = 0
            
    if check == K:
        check = 0
        secondMax = 0
        for j in range(N):
            if j == index:
                continue
            else:
                if array[j] >= secondMax:
                    secondMax = array[j]
                    preIndex = j 
        maximum = secondMax
        
    output += maximum

print(output)

# list.sort()를 이용하여 조금더 효율적으로 진행가능,, 첫번째 두번째 것만을 외우고 두개를 더해줘가면 된다. 