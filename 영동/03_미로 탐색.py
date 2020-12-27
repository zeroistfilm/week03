# https://www.acmicpc.net/problem/2178

N,M = map(int, input().split())

graph=[[] for i in range(N)]
for i in range(N):
    tmp = input()
    for j in range(len(tmp)):
        graph[i].append(int(tmp[j]))


direction = [[0,1],[-1,0],[0,-1],[1,0]]

def bfs(graph,start,visited):
    from collections import deque
    queue = deque([start])
    visited[start[0]][start[1]] = True
    while queue:
        v = queue.popleft()
        for dir in direction:
            tmp = v[:]
            tmp[0] += dir[0]
            tmp[1] += dir[1]
            if tmp[1]<len(graph[0]) and tmp[0]<len(graph) and tmp[1]>=0 and tmp[0]>=0: #그래프의 범위를 넘어가는 경우
                if visited[tmp[0]][tmp[1]]==False and graph[tmp[0]][tmp[1]]!=0:
                    queue.append(tmp)
                    visited[tmp[0]][tmp[1]]=True
                    graph[tmp[0]][tmp[1]]+= graph[v[0]][v[1]]

visited=[[False for i in range(M)]for i in range(N)]
bfs(graph,[0,0],visited)
print(graph[N-1][M-1])


