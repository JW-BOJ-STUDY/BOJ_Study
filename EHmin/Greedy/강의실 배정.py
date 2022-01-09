import sys
import heapq

timeItem = [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline().strip()))]

sortedItem = sorted(timeItem)

heap = []

heapq.heappush(heap, sortedItem.pop(0)[1])

for i in sortedItem:
    if heap[0] <= i[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, i[1])
    else:
        heapq.heappush(heap, i[1])
        
sys.stdout.write(str(len(heap)))