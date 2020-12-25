import sys
from collections import deque
read = sys.stdin.readline
sys.setrecursionlimit(10**8)

n  = int(read())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(n-1):
    node1, node2 = map(int, read().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

parents = [0 for _ in range(n+1)]

# dfs 풀이
# 돌면서 부모를 결정해준다
# def dfs(graph, visited, start, parent):
#     visited[start] = True
#     parents[start] = parent
#     for one in graph[start]:
#         if not visited[one]:
#             dfs(graph, visited, one, start)

def dfs(graph, start, parents):
    for one in graph[start]:
        if not parents[one]:
            parents[one] = start
            dfs(graph, one, parents)


# bfs 풀이
# 돌면서 부모노드가 결정되지 않은 애들의 부모를 결정해준다
# def bfs(graph, visited, start):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         x = queue.popleft()
#         for one in graph[x]:
#             if not parents[one]:
#                 parents[one] = x
#                 queue.append(one)


# bfs(graph, visited, 1)
dfs(graph, 1, parents)
for i in parents[2:]:
    print(i)
