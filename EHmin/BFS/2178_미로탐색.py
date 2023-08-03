from collections import deque
# 입력 받기 
N,M = map(int, input().split())
graph = [list(map(int,input())) for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]

dx = [1 , 0 , -1 , 0]
dy = [0 , 1 , 0 , -1]

def bfs(graph, visited, start):
    visited[start[0]][start[1]] = True
    queue = deque([start])
    
    while queue:
        start = queue.popleft()
        i = start[0] # y...
        j = start[1] # x... 
        visited[i][j] = True
        distance = graph[i][j]
        
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if x<0 or x>=M or y<0 or y>=N:
                continue
            elif not visited[y][x] and graph[y][x] == 1:
                queue.append([y,x])  
                graph[y][x] = distance + 1

bfs(graph, visited, [0,0])

# print(graph)
print(graph[N-1][M-1])
                