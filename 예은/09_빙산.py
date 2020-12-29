import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())
iceberg = []
q = deque()

for i in range(n):
    iceberg.append(list(map(int, read().split())))
    for j in range(1, m-1):
        if iceberg[i][j]:
            q.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 녹일 만큼 덱에 저장
def melt():
    minus = deque()
    while q:
        x, y = q.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if iceberg[nx][ny] == 0: cnt += 1
        minus.append((x, y, cnt))

    while minus:
        x, y, cnt = minus.popleft()
        if cnt:
            iceberg[x][y] -= cnt
            if iceberg[x][y] > 0: q.append((x, y))
            elif iceberg[x][y] < 0: iceberg[x][y] = 0
        else:
            if iceberg[x][y] > 0: q.append((x, y))
    return len(q)


# 방문처리, 빙산인 칸의 개수 세주기
def bfs(x, y):
    ice = deque()
    ice.append((x, y))
    visited[x][y] = True
    count = 1
    while ice:
        x, y = ice.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 < nx < n-1 and 0 < ny < m-1) and iceberg[nx][ny] and not visited[nx][ny]:
                ice.append((nx, ny))
                visited[nx][ny] = True
                count += 1
    return count


year = 0
while True:
    component = 0
    year += 1
    visited = [[0 for _ in range(m)] for _ in range(n)]

    ice_size = melt()

    # 한 해 지나고 빙산 수 세기
    # bfs 한 번 돌려서 빙산인 칸의 수를 확인하는데 큐에 남아있고 전년도와 다르면 빙산이 갈라진거니까 그때 출력하면 됨
    # -> bfs 여러번 돌릴 필요 없음
    for i in range(1, n-1):
        for j in range(1, m-1):
            if iceberg[i][j] and not visited[i][j]:
                start_x, start_y = i, j # bfs 시작점 찾기

    # 녹인 빙산의 크기
    if start_x and start_y:
        one_bfs_size = bfs(start_x, start_y)
        if ice_size != one_bfs_size: # 빙산이 갈라졌어요
            print(year)
            break

    else:
        print(0)
        break

    start_x, start_y = 0, 0

# 이중포문 돌면서 빙하 있고 방문 안했으면 빙하 개수 늘려주고, 녹인다
