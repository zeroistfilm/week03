import sys
from collections import deque
read = sys.stdin.readline

r, c = map(int, read().split())
forest = []
water = deque()
dochi = deque()

# 입력 받으면서 위치 확인
for i in range(r):
    forest.append(list(read().rstrip()))
    for j in range(c):
        if forest[i][j] == 'S':
            dochi_x, dochi_y = i, j
            dochi.append((i, j))
        elif forest[i][j] == '*':
            water.append((i, j))
            forest[i][j] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def water_bfs():
    while water:
        x, y = water.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
            if forest[nx][ny] == '.':
                forest[nx][ny] = forest[x][y] + 1
                water.append((nx, ny))

def dochi_bfs(x, y):
    forest[x][y] = 0
    while dochi:
        x, y = dochi.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
            if forest[nx][ny] == 'X': continue
            elif forest[nx][ny] == 'D':
                return forest[x][y] + 1
            elif forest[nx][ny] == '.' or forest[nx][ny] > forest[x][y] + 1:
                forest[nx][ny] = forest[x][y] + 1
                dochi.append((nx, ny))
    return 'KAKTUS'

water_bfs()
print(dochi_bfs(dochi_x, dochi_y))