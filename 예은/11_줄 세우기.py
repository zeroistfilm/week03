import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

for i in range(m):
    start, end = map(int, read().split())
    graph[start].append(end)
    indegree[end] += 1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

result = []
while q:
    x = q.popleft()
    result.append(str(x))
    for one in graph[x]:
        indegree[one] -= 1
        if indegree[one] == 0:
            q.append(one)

print(' '.join(result))