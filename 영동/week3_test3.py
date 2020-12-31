# https://www.acmicpc.net/problem/1967

import sys
from collections import deque

N = int(sys.stdin.readline())

graph=[[] for _ in range(N+1)]

for i in range(N-1):
    parent, child, weight = map(int, sys.stdin.readline().split())
    graph[parent].append([child,weight])
    #graph[child].append([parent, weight])


visited=[False]*N
parents=[0]*(N+1)
def dfs(graph,v, visited):
    visited[v]=True
    for i in graph[v]: #노드, 웨이트
        if not visited[i[0]]:
            for j in graph[i[0]]:
                dfs(graph,j[0], visited)
                parents[i+1]=[v+1]
                #print(i+1,'의 부모노드는',v+1)
dfs(graph, 1, visited)

