from collections import deque
from sys import stdin, stdout

# 인풋 받기
N, M, V = map(int, stdin.readline().split())
graph = [[] for _ in range(N)]
visited = [False] * N

# 인풋을 인접리스트로 변환 
for i in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(N):
    graph[i].sort()
# DFS >> 재귀 함수에 가깝고 
def dfs(graph, visited, start):
    visited[start] = True
    # print(str(start + 1) + " ")
    dfs_ret.append(start + 1)
    
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, visited, i)

dfs_ret = []
dfs(graph, visited, V-1)


# BFS >> while 문에 가까움
visited = [False] * N
def bfs(graph, visited, start):
    visited[start] = True
    # print(str(start + 1) + " ")
    bfs_ret.append(start + 1)
    queue = deque([start])
    
    while queue:
        start = queue.popleft()
        for i in graph[start]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                # print(str(i + 1) + " ")
                bfs_ret.append(i + 1)
                
bfs_ret = []        
bfs(graph, visited, V-1)

ret = list(map(str,dfs_ret))
print(" ".join(ret))
ret = list(map(str,bfs_ret))
print(" ".join(ret))

# 주석문도 인터 프리트언어에서는 차이를 만들어낸다. >> in, out 함수가 무거운거니..잘 쓰자