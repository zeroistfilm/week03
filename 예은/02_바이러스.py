import sys
from collections import deque
read = sys.stdin.readline

n = int(read())
m = int(read())
connect = [[] for i in range(n+1)]
for i in range(m):
    node1, node2 = map(int, read().split())
    connect[node1].append(node2)
    connect[node2].append(node1)

visited = [False] * (n+1)
result = []

# dfs 풀이
def dfs(graph, visited, start):
    visited[start] = True
    result.append(start)
    for one in graph[start]:
        if not visited[one]:
            dfs(graph, visited, one)

# bfs 풀이
def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    while queue:
        x = queue.popleft()
        result.append(x)
        for one in graph[x]:
            if not visited[one]:
                queue.append(one)
                visited[one] = True


# dfs(connect, visited, 1)
bfs(connect, visited, 1)
print(len(result) - 1)
