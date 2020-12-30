import sys
from collections import deque
read = sys.stdin.readline

n = int(read())
apart = [list(read().rstrip()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0 for _ in range(n)] for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx =  x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and apart[nx][ny] == '1' and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt

result = []
for i in range(n):
    for j in range(n):
        if apart[i][j] == '1' and not visited[i][j]:
            result.append(bfs(i, j))
result.sort()
print(len(result))
for one in result:
    print(one)