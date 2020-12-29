# https://www.acmicpc.net/problem/3055

R, C = map(int, input().split())

map = [[[] for i in range(C)] for i in range(R)]
for i in range(R):
    tmp = input()
    for j in range(C):
        map[i][j] = tmp[j]

visit = [[False for i in range(C)] for i in range(R)]
water=[]
for i in range(R):
    for j in range(C):
        if map[i][j] != '.':
            visit[i][j] = True
        if map[i][j] == 'S':
            start = [i, j]
            map[i][j]=0
        if map[i][j] == 'D':
            destination = [i, j]
        if map[i][j] == '*':
            water.append([i, j])

direction = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(graph, start,water, visit):
    from collections import deque
    water = deque(water)
    Hedgehog= deque([start])
    visit[start[0]][start[1]]=True

    while water or Hedgehog:
        if water:
            for i in range(len(water)):
                w = water.popleft()
                for dir in direction:
                    tmp = w[:]
                    tmp[0] += dir[0]
                    tmp[1] += dir[1]
                    if 0 <= tmp[0] and tmp[0] < R and 0 <= tmp[1] and tmp[1] < C :  # 범위 안에 들어오고
                        if graph[tmp[0]][tmp[1]]=='.' and visit[tmp[0]][tmp[1]]==False:
                            water.append(tmp)
                            visit[tmp[0]][tmp[1]] = True
                            graph[tmp[0]][tmp[1]] = '*'
        if Hedgehog:
            for i in range(len(Hedgehog)):
                h = Hedgehog.popleft()
                for dir in direction:
                    tmp = h[:]
                    tmp[0] += dir[0]
                    tmp[1] += dir[1]
                    if 0 <= tmp[0] and tmp[0] < R and 0 <= tmp[1] and tmp[1] < C :  # 범위 안에 들어오고
                        if graph[tmp[0]][tmp[1]]=='D':
                            #print('도착!!')
                            graph[tmp[0]][tmp[1]] = graph[h[0]][h[1]] + 1
                            return
                        if graph[tmp[0]][tmp[1]]=='.' and visit[tmp[0]][tmp[1]]==False:
                            Hedgehog.append(tmp)
                            visit[tmp[0]][tmp[1]] = True
                            graph[tmp[0]][tmp[1]] = graph[h[0]][h[1]]+1

bfs(map,start,water,visit)
if map[destination[0]][destination[1]]=='D':
    print('KAKTUS')
else:
    print(map[destination[0]][destination[1]])
