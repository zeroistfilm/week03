import sys
from collections import deque
read = sys.stdin.readline

n, m, v = map(int, read().split())
graph = [[]  for _ in range(n+1)]
for i in range(m):
    node1, node2 = map(int, read().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(1, n+1):
    graph[i].sort()

print(graph)

dfs_visited = [False] * (n+1)
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for one in graph[v]:
        if not visited[one]:
            dfs(graph, one, visited)


bfs_visited = [False] * (n+1)
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for one in graph[v]:
            if not visited[one]:
                queue.append(one)
                visited[one] = True


dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)



# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]
#
# visited = [False] * 9
#
#
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#
# dfs(graph, 1, visited)