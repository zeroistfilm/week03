# https://www.acmicpc.net/problem/1260

N, M, V = map(int, input().split())


adjacencymatrix = [[0 for i in range(N)] for i in range(N)]
adjacencyList = [[] for i in range(N)]
for i in range(M):
    nodes = list(map(int, input().split()))
    #인접행렬만들
    adjacencymatrix[nodes[0] - 1][nodes[1] - 1] = 1
    adjacencymatrix[nodes[1] - 1][nodes[0] - 1] = 1
    #인접리스트 만들기
    adjacencyList[nodes[1] - 1].append(nodes[0]-1)
    adjacencyList[nodes[0] - 1].append(nodes[1]-1)


def dfs(graph,v,visited):
    visited[v] = True
    print(v+1, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,v,visited):
    from collections import deque
    queue = deque([v])
    visited[v] = True
    while queue:
        a=queue.popleft()
        print(a+1,end=' ')
        for i in sorted(graph[a]):
            if not visited[i]:
                queue.append(i)
                visited[i]=True

visited = [False for i in range(N)]
dfs(adjacencyList,V-1,visited)
print()
visited2 = [False for i in range(N)]
bfs(adjacencyList,V-1,visited2)
