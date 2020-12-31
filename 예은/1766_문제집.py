import sys
from collections import deque
import heapq
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
for i in range(m):
    node1, node2 = map(int, read().split())
    graph[node1].append(node2)
    indegree[node2] += 1

q = []
result = []
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

while q:
    x = heapq.heappop(q)
    result.append(x)
    for one in graph[x]:
        indegree[one] -= 1
        if indegree[one] == 0:
            heapq.heappush(q, one)

print(*result)