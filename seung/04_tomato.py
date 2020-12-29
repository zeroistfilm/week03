import sys
from collections import deque
sys.stdin = open("./seung/input.txt","r")
M,N,H = map(int,sys.stdin.readline().split())
matrix = [[list(map(int,sys.stdin.readline().split())) for _ in range(N)] for i in range(H)]
visit_map = [[[0 for _ in range(M)] for _ in range(N) ]for _ in range(H)] # 높이로 먼저 반복 돌리고 그 다음 행,열 순서로 반복 돌리면 됨.

queue = deque([])

for h in range(H):
    for row in range(N):
        for col in range(M):
            if matrix[h][row][col] == 1:
                queue.append([row,col,h]) # 1로 되어있는 정점은 미리 3차원 맵에 담아놓기

# 일단 돌면서 6방향이 -1로 가득차진 않았는지 확인해보다가, 1이 나오면 그때부터 BFS로 탐색
dx = [-1,0,1,0,0,0] # 순서대로 좌, 상, 우, 하,위,아래
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs(matrix,queue):
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            next_x = x + dx[i]
            next_y = y + dy[i]
            next_z = z + dz[i]
            # 바깥에 나가거나 -1인 거는 스킵.
            if next_x < 0 or next_x >= N or \
                next_y < 0 or next_y >= M or \
                next_z < 0 or next_z >= H or \
                matrix[next_z][next_x][next_y] != 0 or \
                visit_map[next_z][next_x][next_y] >= 1:
                continue
            # matrix[next_z][next_x][next_y] = 1
            # visit_map[next_z][next_x][next_y] = visit_map[z][x][y] + 1
            matrix[next_z][next_x][next_y] = matrix[z][x][y] + 1
            visit_map[next_z][next_x][next_y] = 1
            queue.append([next_x, next_y,next_z])

bfs(matrix, queue)
max_num = 0
isTrue= False
# 처음부터 익어있는지, 모두 익지 못하는지, 토마토가 모두 익을 수 있으면 며칠 걸리는지 판별하기
# flag = False
for z in range(H):
    for x in range(N):
        for y in range(M):
            if matrix[z][x][y] == 0:
                isTrue = True
            max_num = max(max_num,matrix[z][x][y])
if isTrue == True:
    print(-1)
else:
    print(max_num-1)
