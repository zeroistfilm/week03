import sys
from collections import deque, defaultdict
read = sys.stdin.readline

n = int(read())
m = int(read())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
for i in range(m):
    start, end, num = map(int, read().split())
    graph[start].append([end, num])
    indegree[end] += 1

q = deque()
base = []
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
    if not graph[i]: base.append(i)

result = defaultdict(int)
while q:
    x = q.popleft()
    if result[x] == 0: result[x] = 1
    for i in range(len(graph[x])):
        result[graph[x][i][0]] += graph[x][i][1] * result[x]
        indegree[graph[x][i][0]] -= 1
        if indegree[graph[x][i][0]] == 0:
            q.append(graph[x][i][0])

for one in base:
    print(one, result[one])







