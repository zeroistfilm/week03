import sys
from collections import deque
sys.setrecursionlimit(10**8)
sys.stdin = open("./seung/input.txt","r")
ROW, COL = map(int,sys.stdin.readline().split())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(ROW)]

# 큐에 0과 인접한 1만 넣기
que = deque([])
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs_iceberg(matrix,i,j) -> None:
    if 0<= i < ROW and 0<= j < COL and matrix[i][j] == 0:

        matrix[i][j] = '*'
        dfs_iceberg(matrix,i+1,j) # 재귀로 인접한 영역 탐색(아래쪽 방향)
        dfs_iceberg(matrix,i-1,j) # 재귀로 인접한 영역 탐색(위쪽 방향)
        dfs_iceberg(matrix,i,j+1) # 재귀로 인접한 영역 탐색(오른쪽 방향)
        dfs_iceberg(matrix,i,j-1) # 재귀로 인접한 영역 탐색(왼쪽 방향)


def melt():
    for i in range(ROW):
        for j in range(COL):
            if matrix[i][j] == 1:
                que.append([i, j])
    melted=[]
    while que:
        x,y = que.popleft()
        cnt = 0
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if matrix[next_x][next_y] == '*':
                cnt+=1
                if cnt>=2:
                    matrix[x][y] = 0
                    if [x,y] not in melted:
                        melted.append([x,y])

    if len(melted)>0:
        for a,b in melted:
            dfs_iceberg(matrix,a,b)
    return melted

dfs_iceberg(matrix,0,0)
time = 0
past_lst = 0

while True:
    melted_lst = melt()
    if len(melted_lst) == 0:
        print(time)
        break
    if len(melted_lst) > 0:
        time+=1
