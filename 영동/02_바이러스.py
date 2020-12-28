# https://www.acmicpc.net/problem/2606

N = int(input()) #컴퓨터 수
edge = int(input())

adlist = [[] for i in range(N)]
for i in range(edge):
    x, y = map(int, input().split())
    adlist[x - 1].append(y - 1)
    adlist[y - 1].append(x - 1)

infected=0

def bfs(graph,start,visited,infected):
    from collections import deque
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        #print(v+1, end=' ')
        infected+=1
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i]=True
    return infected

visited=[False for i in range(N)]
infected=bfs(adlist,0,visited,infected)
print(infected-1)