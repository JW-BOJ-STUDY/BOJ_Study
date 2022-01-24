N = int(input())
list1 = [] 

for i in range(N):
    list1.append(int(input()))
list1.sort()

result = 0 

for i in range(len(list1)):
    if result < N*list1[i]:
        result = N*list1[i]
        N-=1
    else:
        N-=1
print(result)
