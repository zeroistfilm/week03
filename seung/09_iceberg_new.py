import sys
from collections import defaultdict
sys.stdin = open("./seung/input.txt","r")
def melt():
    melting_area = {}  # 녹일 곳
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[0] * M for _ in range(N)]  # 방문하는 지역 세팅. 빙산 리스트가 갱신될 때마다 이것도 새롭게 만들어야 함. (기존꺼 쓸 수 없음.)
    stack = [] # DFS 구현을 위해 스택 생성
    stack.append(iceberg[0]) # 1번째 빙산을 스택에 넣어 줌.
    cnt_for_melting = 0  # 녹이는 대상이 되는 빙산들 개수 ( 나중에 전체 빙산과 비교해서 한덩어리인지 확인 )
    visited[iceberg[0][0]][iceberg[0][1]] = 1 # 스택에서 뺀 빙산들은 탐색을 위해 방문을 한거니까 빙산 리스트에 있는 첫 원소부터 시작처리

    # 첫 빙산 가지고오기 -> 녹임 -> 한번 녹인 빙산 가지고오기 -> 녹임 -> .. 반복
    while stack: # 스택에 빙산 하나를 넣고 붙어있으면 그 붙어있는 빙산이 스택에 넣어지면서 계속 탐색이 되는데,만약에 인접한 빙산이 없으면(고립된 빙산), 스택이 1개에서 멈추게 되고 1개 처리되고 종료됨.
        x, y = stack.pop()
        cnt_for_melting += 1
        # 스택에서 꺼낼 때 마다 탐색할 빙산의 개수를 +1 증가
        melt_height = 0
        for k in range(4):
            next_x = x + dx[k]
            next_y = y + dy[k]
            if matrix[next_x][next_y] != 0 and visited[next_x][next_y] == 0 :  # 4방향 중 하나가 빙산이면
                stack.append((next_x, next_y)) # 스택에 다음 탐색 빙산 넣고
                visited[next_x][next_y] = 1 # 방문했다는 표시

            elif matrix[next_x][next_y] == 0:  # 4방향이 바다이면
                melt_height += 1
        melting_area[(x, y)] = melt_height # 빙산의 좌표 넣고, 녹여야 하는 수(인접 바다 수) 값으로 넣기
    # 녹이는 과정
    new_iceberg = []  # 새로운 빙산으로 바꾸기 위해 리스트 하나 만듬.
    for key, value in melting_area.items():
        i, j = key
        matrix[i][j] = max(0, matrix[i][j] - value) # 0보다 작으면 0으로 인식
        if matrix[i][j] > 0: # 녹여도 빙하가 남아있으면 빙하 다시 추가
            new_iceberg.append((i, j))

    return cnt_for_melting, new_iceberg


N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 탐색을 위해 빙산 좌표만 먼저 찾아서 큐 혹은 스택에 넣기
iceberg = []
for i in range(N):
    for j in range(M):
        if matrix[i][j]:
            iceberg.append((i, j))

year = 0
while True: # 위에서 전처리하고 본격적으로 빙산녹이고 덩어리 개수 찾는 로직
    # selected_cnt: 녹인 개별 빙산의 개수
    # new_iceberg : 녹인 후의 빙산 리스트
    cnt_for_melting, new_iceberg = melt()
 # 한덩어리인지 체크(녹여야하는 빙산 개수랑 녹이기 전 빙산 개수랑 같으면 한 덩어리라는 것 = 한번의 DFS 탐색으로도 다 닿을 수 있으니 한 덩어리)
    if cnt_for_melting != len(iceberg):
        break

# 녹이는 빙산의 개수가 0이고 녹인 후의 빙산이 안 남았으면(빙산이 녹을 때까지 분리되지 않으면)
    if cnt_for_melting == 0 or len(new_iceberg) == 0:
        year = 0
        break
# 빙산 리스트를 녹인 후 빙산 리스트로 교체하고 년도 증가
    iceberg = new_iceberg[:]
    year += 1


print(year)
