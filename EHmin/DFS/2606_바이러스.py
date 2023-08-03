# input 받아오기 
c_num = int(input().strip())
graph = [[] for i in range(c_num)]
# graph = [[]] * c_num 이랑 똑같음 >> 겉모습은 똑같은데 이렇게 진행하면 레퍼런스도 공유하는 모양
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
    

    