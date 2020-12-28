# https://www.acmicpc.net/problem/11725

import sys
sys.setrecursionlimit(100000) #런타임 에러 방지
N = int(input())
adjList = [[] for i in range(N)]

for i in range(N-1):
    a= sorted(list(map(int, input().split())))
    adjList[a[0] - 1].append(a[1] - 1)
    adjList[a[1] - 1].append(a[0] - 1)

visited=[False]*N
parents=[0]*(N+1)
def dfs(graph,v, visited):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i, visited)
            parents[i+1]=[v+1]
            #print(i+1,'의 부모노드는',v+1)
dfs(adjList, 0, visited)
for i in range(len(parents)):
    if not parents[i]==0:
        print(parents[i][0])