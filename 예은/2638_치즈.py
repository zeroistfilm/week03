import sys
from collections import deque
read = sys.stdin.readline

# 0,0부터 bfs탐색하면서 겉에만 녹이기
n, m = map(int, read().split())
cheese = [list(read().split()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 0,0 에서 bfs시작해서 뻗어나가면서 뻗어나간 좌표에서 주변 1 있는지 확인한다. 뻗어나가는 사방, 확인하는 사방 2개 있어야함
def bfs(x, y):
    cnt = 0
    nocheese = deque()
    nocheese.append((x, y))
    while nocheese:
        x, y = nocheese.popleft()
        visited[x][y] = 1
        # 사방으로 뻗어나가는 bfs
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 치즈가 없으면 nocheese 큐에 담음
            if 0 <= nx < n and 0 <= ny < m and cheese[nx][ny] == '0' and not visited[nx][ny]:
                visited[nx][ny] = 1
                nocheese.append((nx, ny))
                for j in range(4):
                    nnx = nx + dx[j]
                    nny = ny + dy[j]
                    # 치즈가 없는 곳에서 주변에 치즈가 있으면 그 치즈 좌표가 녹일 치즈니까 큐에 담음
                    if 0 <= nnx < n and 0 <= nny < m and cheese[nnx][nny] == '1' and not visited[nnx][nny]:
                        visited[nnx][nny] = 1
                    elif 0 <= nnx < n and 0 <= nny < m and cheese[nnx][nny] == '1' and visited[nnx][nny]:
                        cheese[nnx][nny] = '0'
                        cnt += 1
    return cnt


hour = 0
while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    new_cheese_sum = bfs(0, 0)

    if new_cheese_sum == 0:
        print(hour)
        break

    cheese_sum = new_cheese_sum
    hour += 1

