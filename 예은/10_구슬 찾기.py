import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())
indegree = [[] for _ in range(n+1)] # 노드보다 무거운 애들이 값
outdegree = [[] for _ in range(n+1)] # 노드보다 가벼운 애들이 값
for i in range(m):
    node1, node2 = map(int, read().split())
    indegree[node2].append(node1)
    outdegree[node1].append(node2)

def dfs(start, graph, visited, temp):
    visited[start] = True
    temp.append(start)
    for one in graph[start]:
        if not visited[one]:
            dfs(one, graph, visited, temp)


cnt = 0
for i in range(1, n+1):
    visited_in = [False] * (n + 1)
    visited_out = [False] * (n + 1)
    temp_in = []
    temp_out = []
    dfs(i, indegree, visited_in, temp_in)
    dfs(i, outdegree, visited_out, temp_out)
    if len(temp_in) > (n+1)//2: cnt += 1
    if len(temp_out) > (n+1)//2: cnt += 1

print(cnt)


