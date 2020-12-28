import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int, read().split())
iceberg = []
minus = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    iceberg.append(list(map(int, read().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def one_year(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        if iceberg[nx][ny] == 0: cnt += 1
    iceberg[x][y] = (iceberg[x][y] - cnt) if (iceberg[x][y] - cnt) >= 0 else 0

# 방문처리
def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n and 0 <= ny < m) and iceberg[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)
            return True
    return False


component = 0
year = 0
year += 1
# 한 해가 지났을 때의 결과
for i in range(n):
    for j in range(m):
        if iceberg[i][j]:
            one_year(i, j)

print(minus)

# 한 해 지나고 빙산 수 세기
for i in range(n):
    for j in range(m):
        if iceberg[i][j] and not visited[i][j]:
            if dfs(i,j):
                component += 1

# if component >= 2 or component == 0: break

print(year if component >= 2 else 0)
