import sys
from collections import deque
sys.stdin = open("./seung/input.txt","r")
ROW,COL = map(int,sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().strip()) for _ in range(ROW)]
visit_map = [[0] * COL for _ in range(ROW)]

queue = deque()
for row in range(ROW):
    for col in range(COL):
        if matrix[row][col] == '*':
            # 물 먼저 다 넣고 고슴도치 front에 넣기
            queue.append([row,col])
        elif matrix[row][col] == 'S':
            # matrix[row][col] = 0
            hodgedog = [row,col]
        elif matrix[row][col] == 'D':
            bv_r, bv_c = row,col

queue.appendleft(hodgedog)

dx = [-1,0,1,0] # 순서대로 좌, 상, 우, 하
dy = [0,1,0,-1]
def bfs(matrix,queue):
    flag = False
    while queue:
        x,y = queue.popleft()
        if flag: # 고슴도치가 D에 도착했으면
            break
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            # 고슴도치 - 바깥에 나가거나 돌, 물 지역은 가면 안됨.
            if 0<= next_x < ROW and 0 <= next_y < COL:
                # (물 입장에서)다음에 갈 지역이 비어있는 곳이고 비버 동굴이 아니면 물 영역을 확장한다.
                if matrix[x][y] == '*':
                    if matrix[next_x][next_y] == '.' or matrix[next_x][next_y] == 'S':
                        matrix[next_x][next_y] = '*'
                        queue.append([next_x,next_y])
                # (고슴이 입장에서) 다음에 갈 지역이 비어있고, 물이 아니고 바위가 아니고, 맵 상 이미 방문한 곳이 아니면 visit map에 이동 거리를 찍는다.
                elif matrix[x][y] == 'S':
                    print(matrix)
                    if matrix[next_x][next_y] == '.':
                        matrix[next_x][next_y] = 'S'
                        visit_map[next_x][next_y] = visit_map[x][y] +1
                        queue.append([next_x, next_y])
                    elif matrix[next_x][next_y] == 'D': #고슴도치가 D에 도착할 수 있으면
                        flag = True
                        visit_map[next_x][next_y] = visit_map[x][y]+1
                        break
bfs(matrix,queue)
if visit_map[bv_r][bv_c] == 0:
    print('KAKTUS')
else:
    print(visit_map[bv_r][bv_c])