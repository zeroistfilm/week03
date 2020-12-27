import sys,copy
from typing import List
from collections import deque
from itertools import chain
sys.stdin = open("./seung/input.txt","r")
N,M = map(int, sys.stdin.readline().split())
matrix = [ list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def dfs_iceberg(grid: List[List[int]], i: int, j:int) -> None:
    if 0<= i < N and 0<= j < M and grid[i][j] >= 1 and visited[i][j] != 1:

        visited[i][j] = 1
        dfs_iceberg(grid,i+1,j) # 재귀로 인접한 영역 탐색(아래쪽 방향)
        dfs_iceberg(grid,i-1,j) # 재귀로 인접한 영역 탐색(위쪽 방향)
        dfs_iceberg(grid,i,j+1) # 재귀로 인접한 영역 탐색(오른쪽 방향)
        dfs_iceberg(grid,i,j-1) # 재귀로 인접한 영역 탐색(왼쪽 방향)

dx = [-1,0,1,0] # 순서대로 좌, 상, 우, 하
dy = [0,1,0,-1]

def bfs(matrix,queue):
    flag = False
    while queue:
        x,y = queue.popleft()
        count = 0
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0<= next_x < N and 0 <= next_y < M:
                    if matrix[next_x][next_y] == 0:
                        count +=1
                        # queue.append([next_x,next_y])
        result = matrix[x][y] - count
        if result < 0:
            cpy_matrix[x][y] = 0
        else:
            cpy_matrix[x][y] = result
year = 0
cpy_matrix = copy.deepcopy(matrix)
for _ in range(300):
    iceberg_cnt = 1
    visited = []
    queue = deque([])
    for row in range(N):
        visited.append([0] * M)
    for row in range(N):
        for col in range(M):
            # 온전한 빙산 개수 세기
            if matrix[row][col] >= 1 and visited[row][col] == 0:
                dfs_iceberg(matrix,row,col)
                iceberg_cnt += 1
            # 빙산 큐에 넣기
            if matrix[row][col] > 0:
                queue.append([row, col])
    bfs(matrix,queue)
    matrix = copy.deepcopy(cpy_matrix)
    year+=1
    result = all(x == 0 for x in chain(*matrix))
    if iceberg_cnt >=2:
        print(year)
        break
    if result:
        print(0)
        break

