from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]
#bfs
def bfs(graph, start): #들어오는 start를 i,j로 받아줄것 
    queue = deque([start])
    graph[start[0]][start[1]] = 0
    ret = 1
    
    while queue:
        index = queue.popleft()
        x = index[0]
        y = index[1]
        
        for k in range(4):
            a = x + dx[k]
            b = y + dy[k] 
            
            if a < 0 or a >= N or b < 0 or b >= N: #제약 조건
                continue
            
            elif graph[a][b] == 1:
                queue.append([a,b])
                graph[a][b] = 0 # 미리 방문처리를 하면 메모리의 이득을 볼 수 있다. 
                ret += 1

    return ret

N = int(input())
graph = [list(map(int,input())) for _ in range(N)] # 문자열을 list만 해줘도 알아서 나눌수 있음!
ret = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            ret.append(bfs(graph, [i,j]))
            
print(len(ret))
ret.sort()
for i in ret:
    print(i)
    
# 방문 처리의 위치를 바꾸면 메모리 부족 문제를 해결할 수 있었음 