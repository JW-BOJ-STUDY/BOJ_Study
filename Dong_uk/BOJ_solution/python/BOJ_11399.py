N = int(input()) # 사람 수 
list = list(map(int,input().split())) # 인출 시간

list.sort()

for i in range(1, N) :
    list[i] += list[i-1]

print(sum(list))


