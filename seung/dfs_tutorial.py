import sys
from typing import List
sys.stdin = open("./seung/input.txt","r")
n = int(input())
matrix = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

def dfs(grid: List[List[str]], i: int, j:int) -> None:
    # 탐색 인덱스가 바깥쪽일 경우
    if i < 0 or i >= len(grid[0]) or \
            j < 0 or j >=len(grid[0]) or \
            grid[i][j] != 1: # 탐색 인덱스가 섬이 아닌 경우
        return

    grid[i][j] = '#' # 이미 탐색이 된 인덱스는 # 등의 다른 부호로 바꿔주어 이미 방문을 했다는 표시를 남긴다. 이러면 다시 계산할 필요가 없게 된다.(가지치기)

    # 호출 됐는데 위의 조건에 걸리면 리턴되면서 종료된다. (백트래킹으로 빠져나와 그 전 지점으로 돌아온다.)
    dfs(grid,i+1,j) # 재귀로 인접한 영역 탐색(아래쪽 방향)
    dfs(grid,i-1,j) # 재귀로 인접한 영역 탐색(위쪽 방향)
    dfs(grid,i,j+1) # 재귀로 인접한 영역 탐색(오른쪽 방향)
    dfs(grid,i,j-1) # 재귀로 인접한 영역 탐색(왼쪽 방향)

if not matrix: # 행렬이 없는 경우 예외처리
    exit()

count = 0 # 섬 개수를 위한 변수

for i in range(len(matrix)): # 행을 탐색
    for j in range(len(matrix[0])): # 열을 탐색
        if matrix[i][j] == 1: # 한 줄씩 탐색하면서 현재 위치가 섬이면
            dfs(matrix,i,j) # dfs 호출해서 상하좌우도 섬인지 탐색
            count+=1 #위의 함수(재귀 포함)를 다 돌고 더 이상 돌릴 재귀가 없으면 카운트를 +1

print(count)


