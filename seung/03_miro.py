import sys
from typing import List
from collections import defaultdict,deque
sys.stdin = open("./seung/input.txt","r")

N,M = map(int,sys.stdin.readline().split())
# 매트릭스는 값만 받아놓자. 처음에는 좌표를 같이 받으려했는데 생각해보니 좌표는 큐에만 넣고 큐의 [i][j]요소를 이용해 matrix의 값을 가지고 오면 된다.
# 매트릭스는 고정되어있으니까?
matrix = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

# 상하좌우 방향 탐색할 때는 진짜 웬만하면 dx, dy부터 생각하고 보자.
dx = [-1,0,1,0] # 순서대로 좌, 상, 우, 하
dy = [0,1,0,-1]
# visit을 행렬로 만들어서, 1은 방문한 거, 1 이상은 그 지점까지의 거리로 판단하자.
visit_map = [[0] * M for _ in range(N)]

visit_map[0][0] = 1 #시작점은 출발할 때 여기 찍었다고 표기해줘야 함. 안 그러면 나중에 다시 돌아올 수 있음.
# 큐에 첫 좌표 넣기
queue = deque([[0,0]])

while queue:
    # 현재 지점의 행렬 좌표
    x,y = queue.popleft()
    # 상하좌우로 탐색, 4방향이니까 4
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        # 그 다음 지점을 큐에 넣기 전에 중복 혹은 범위를 넘었는지 체크해야 함.
        # 지나간 지점은 1 아닌 거로 두고 1 아닌 것만 계속 탐색하는 건데, 한번만 방문하는 꼴이 되는데 만약에 큐에서 front를 뺀 다음 그 지점의 다음 거리가 구해졌고
        # 그 뒤에 어떤 front를 빼서 그 지점으로 갈 수 있지만 이미 방문한거라 거리를 갱신 못하는 상황이라는건 이미 있던 거리보다 더 길다는 것을 뜻한다.
        # 트리 계층 상 가장 빨리 도착한 레벨이 결국 최단경로를 계속 만들어내는 거다. 인위적으로 상하좌우 움직인 이후 위 단계랑 비교할 필요가 없는거.
        if next_x < 0 or next_x >= N or \
                next_y < 0 or next_y >= M or \
            matrix[next_x][next_y] < 1 or \
            visit_map[next_x][next_y] > 0:
            continue

        # 다음 지점의 거리는 현재까지의 거리 +1이 되어야 함.
        visit_map[next_x][next_y] = visit_map[x][y] + 1
        # BFS를 위해 큐에 다음 탐색 지점(인접행렬에 대응되는 지점)을 넣어준다.
        queue.append([next_x, next_y])

# 마지막 지점의 거리를 출력
print(visit_map[N-1][M-1])
