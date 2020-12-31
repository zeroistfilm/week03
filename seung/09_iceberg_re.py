import sys
from collections import deque
sys.stdin = open("./seung/input.txt","r")
N,M = map(int,sys.stdin.readline().split())

matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# 빙산을 다 넣는다.

def melt_iceberg():
    queue = deque([])
    visited = [[0] * M for _ in range(N)]
    queue.append(iceberg[0])
    visited[iceberg[0][0]][iceberg[0][1]] = 1

    melting_area = {}
    melted_ice_cnt = 0
    dx = [-1, 0, 1, 0]  # 순서대로 좌, 상, 우, 하
    dy = [0, 1, 0, -1]
    while queue:
        melting_height = 0
        x,y = queue.popleft()
        melted_ice_cnt += 1
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0 <= next_x < N and 0<= next_y <M and matrix[next_x][next_y] == 0:
                melting_height +=1
            elif matrix[next_x][next_y] !=0 and visited[next_x][next_y] == 0:
                visited[next_x][next_y] = 1
                queue.append([next_x, next_y])

        melting_area[(x,y)] = melting_height

    new_iceberg= []

    for k,v in melting_area.items():
        i,j = k
        matrix[i][j] = max(0, matrix[i][j]- v )
        if matrix[i][j] > 0:
            new_iceberg.append([i,j])
    return melted_ice_cnt, new_iceberg

year=0

# 처음 만든 한 덩어리 빙산을 세팅
iceberg = []
for i in range(N):
    for j in range(M):
        if matrix[i][j]:
            iceberg.append((i, j))

while True:
    cnt, new_ice = melt_iceberg()
    if cnt != len(iceberg): # 처음 만든 빙산에서 덩어리가 깨졌는지
        break
    if cnt == 0 or len(new_ice) == 0 :
        year= 0
        break

    iceberg = new_ice[:]
    year+=1

print(year)