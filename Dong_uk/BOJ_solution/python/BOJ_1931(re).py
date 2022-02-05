import sys 

N = int(sys.stdin.readline())
list = [[0]*2 for i in range(N)]

for i in range(N):
    n,m = map(int,sys.stdin.readline().split())
    list[i][0] = n
    list[i][1] = m

# list.sort(key = lambda x: (x[1], x[0]))
# cnt = 1 
# end_time = list[0][1] 
# for i in range(1, N): 
#     if list[i][0] >= end_time:
#          cnt += 1 
#          end_time = list[i][1] 
# print(cnt)
