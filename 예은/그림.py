import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())
paper = [list(read().rstrip().split()) for _ in range(n)]
# visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y):
    area = 0
    q = deque()
    q.append((x, y))
    paper[x][y] = '0'
    while q:
        x, y = q.popleft()
        area += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if paper[nx][ny] == '0': continue
            else:
                paper[nx][ny] = '0'
                q.append((nx, ny))
    return area


cnt, max_area = 0, 0
for i in range(n):
    for j in range(m):
        if paper[i][j] == '1':
            area = bfs(i, j)
            cnt += 1
            if max_area < area:
                max_area = area

print(cnt)
print(max_area)

