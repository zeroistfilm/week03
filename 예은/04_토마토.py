# 3차원 배열 (x, y, z)
import sys
from collections import deque
read = sys.stdin.readline

m, n, h = map(int, read().split())
tomato = []
queue = deque()
fresh = 0
day = 0
# 내 풀이 2 (day를 큐에 같이 넣자) (파이파이 통과, 파이썬 시간초과) (이 방법이 시간, 메모리 더 듦)
for k in range(h):
    temp1 = []
    for i in range(n):
        temp2 = list(read().rstrip().split())
        for j in range(m):
            if temp2[j] == '0':
                fresh += 1
            if temp2[j] == '1':
                queue.append((j, i, k, 0))
        temp1.append(temp2)
        temp2 =[]
    tomato.append(temp1)
    temp1 = []

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
while queue:
    x, y, z, day = queue.popleft()
    for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h:
                continue
            elif tomato[nz][ny][nx] == '-1' or tomato[nz][ny][nx] == '1':
                continue
            elif tomato[nz][ny][nx] == '0':
                tomato[nz][ny][nx] = '1'
                queue.append((nx, ny, nz, day+1))
                fresh -= 1
if fresh:
    print(-1)
else:
    print(day)


# 내 풀이 1 (파이파이 통과, 파이썬 시간초과)
# 배열 입력
# for k in range(h):
#     temp1 = []
#     for i in range(n):
#         temp2 = list(read().rstrip().split())
#         for j in range(m):
#             if temp2[j] == '0':
#                 fresh += 1
#             if temp2[j] == '1':
#                 queue.append((j, i, k))
#         temp1.append(temp2)
#     tomato.append(temp1)
#
# dx = [1, -1, 0, 0, 0, 0]
# dy = [0, 0, 1, -1, 0, 0]
# dz = [0, 0, 0, 0, 1, -1]
#
# while queue and fresh:
#     for _ in range(len(queue)):
#         x, y, z = queue.popleft()
#         for i in range(6):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             nz = z + dz[i]
#             if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h:
#                 continue
#             elif tomato[nz][ny][nx] == '-1':
#                 continue
#             elif tomato[nz][ny][nx] == '0':
#                 tomato[nz][ny][nx] = '1'
#                 queue.append((nx, ny, nz))
#                 fresh -= 1
#     day += 1
#
# if fresh:
#     print(-1)
# else:
#     print(day)