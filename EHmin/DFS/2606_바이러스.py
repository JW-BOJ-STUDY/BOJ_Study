# input 받아오기 
c_num = int(input().strip())
graph = [[] for i in range(c_num)]
visited = [False] * c_num

#input을 인접리스트로 표현하기 
for _ in range(int(input().strip())):
    node_A, node_B = map(int, input().split())
    graph[node_A -1].append(node_B -1)
    graph[node_B -1].append(node_A -1)

def dfs(graph, start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited)

dfs(graph, 0, visited)

ret = 0
for flag in visited:
    if flag:
        ret += 1

print(ret-1)
    

    