import sys 
import heapq

N = int(input())
list = [] 
list2 = [] 
for i in range(N):
    list.append(list(map(int,input().split())))

list.sort()
heapq.heappush(list2, list[0][1])

for i in range(1,N):
    x,y = list[i][0], list[i][1]
    if list[0] <= x :
        heapq.heappop(list2)
        heapq.heappush(list2, y)
    else :
        heapq.heappush(list2, y)
print(len(list2))
