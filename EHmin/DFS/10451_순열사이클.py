N = int(input())

def dfs(graph, visited, start):
    visited[start] = True
    if not visited[graph[start]]:
        visited[graph[start]] = True
        dfs(graph, visited, graph[start])

for _ in range(N):
    number = int(input().strip())
    graph = list(map(lambda x: int(x) - 1, input().split())) #map에 람다 사용할 수 있음. 
    visited = [False] * number
    
    ret = 0
    
    for i in range(number):
        if not visited[i]:
            dfs(graph, visited, i)
            ret += 1
            
    print(ret)
    