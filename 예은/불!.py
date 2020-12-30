import sys
from collections import deque
read = sys.stdin.readline

r, c = map(int, read().split())
maze = []
fire_q = deque()
jihoon_q = deque()
for i in range(r):
    maze.append(list(read().rstrip()))
    for j in range(c):
        if maze[i][j] == 'F':
            fire_q.append((i, j))
            maze[i][j] = 0
        elif maze[i][j] == 'J':
            jihoon_q.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def fire_bfs(queue):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
            if maze[nx][ny] == '#': continue
            elif maze[nx][ny] == '.' or maze[nx][ny] == 'J':
                maze[nx][ny] = maze[x][y] + 1
                fire_q.append((nx, ny))

def jihoon_bfs(queue):
    maze[queue[0][0]][queue[0][1]] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c: # 탈출 성공
                return maze[x][y] + 1
            if maze[nx][ny] == '#': continue
            elif maze[nx][ny] == '.' or maze[nx][ny] > maze[x][y] + 1:
                maze[nx][ny] = maze[x][y] + 1
                jihoon_q.append((nx, ny))
    return 'IMPOSSIBLE'

fire_bfs(fire_q)
print(jihoon_bfs(jihoon_q))



