import sys
from collections import deque
read = sys.stdin.readline

m, n = map(int, read().split())
tomato = []
for i in range(n):
    tomato.append(list(map(int, read().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# bfs의 레벫이 답
# 1인 칸부터 시작해서 쭉쭉 1로 바꿔나간다
# -1인 칸은 1로 못바꾼다
# 토마토가 여러 개인 경우?
# 처음에 토마토 몇 개인지 세고 초기 토마토 다 append 해놓고 시작
def bfs(arr):
    queue = deque(arr)
    while queue:
        x, y, day = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if tomato[ny][nx] == -1:
                continue
            if not tomato[ny][nx]:
                tomato[ny][nx] = 1
                queue.append((nx, ny, day+1))
    return day


start = []
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            start.append((j, i, 0)) # 좌표와 날짜를 포함한 정보

answer = bfs(start)
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            answer = -1
            break
    if answer == -1:
        break

print(answer)


