# https://www.acmicpc.net/problem/7569

M,N,H = map(int, input().split())

basket = [[[]for i in range(N)] for i in range(H)]
for j in range(H):
    for i in range(N):
        basket[j][i]=list(map(int,input().split()))

direction = [[0,1,0],[-1,0,0],[0,-1,0],[1,0,0],[0,0,1],[0,0,-1]] #행,열,높이

def check_ferment(array):
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if array[i][j][k]==0:
                    return False
    return True


def bfs(graph,visited):
    from collections import deque
    queue = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k]==1:
                    queue.append([i,j,k])
                    visited[i][j][k]=True
    while queue:
        v=queue.popleft()
        for dir in direction:
            tmp = v[:]
            tmp[0] += dir[0]
            tmp[1] += dir[1]
            tmp[2] += dir[2]
            if 0<=tmp[0] and tmp[0]<H and 0<=tmp[1] and tmp[1]<N and 0<=tmp[2] and tmp[2]<M: #범위 안에 들어오고
                if visited[tmp[0]][tmp[1]][tmp[2]]==False and graph[tmp[0]][tmp[1]][tmp[2]]==0:
                    queue.append([tmp[0],tmp[1],tmp[2]])
                    visited[tmp[0]][tmp[1]][tmp[2]]=True
                    graph[tmp[0]][tmp[1]][tmp[2]] += graph[v[0]][v[1]][v[2]]+1
    return graph

if not check_ferment(basket):

    visited = [[[False for _ in range(M)]for _ in range(N)]for _ in range(H)]
    after_ferment=bfs(basket,visited)
    #print(after_ferment)
    if not check_ferment(after_ferment):
        print(-1)
    else:
        day=max(max(max(after_ferment)))
        if day>2:
            print(day-1)
        else:
            print(day)


else:
    print(0) #다 익었을 경우

