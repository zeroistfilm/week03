import sys
from collections import deque
read = sys.stdin.readline

n = int(read())
target_a, target_b = map(int, read().split())
m = int(read())
graph = [[] for _ in range(n+1)]
for i in range(m):
    node1, node2 = map(int, read().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# 내 첫 풀이 DFS
# visited = [0] * (n+1)
# # 1촌 관계가 그래프에 담겨있음
# def dfs(start, target, cnt):
#     visited[start] = 1
#     cnt += 1 # 포문 돌기전에 촌수 하나 늘려줘야 형제 셀 때 계속 촌수 늘어나지 않음 (순서에 따라 촌수가 달라지는 문제 해결)
#     for one in graph[start]:
#         if visited[one] == 0:
#             visited[one] = 1
#             if one == target:
#                 print(cnt)
#                 exit() # 타겟에 도착하면 촌수 프린트하고 종료
#             else:
#                 dfs(one, target, cnt) # 타겟 도착못하면 계속 탐색
#
# dfs(target_a, target_b, 0)
# print(-1) # 종료 안돼고 여기까지 왔으면 연결안되있는거

# 남의 풀이 참고 BFS
visited = [0] * (n+1)
distance = [-1] * (n+1)
q = deque()
q.append(target_a)
distance[target_a] = 0
while q:
    x = q.popleft()
    visited[x] = 1
    for one in graph[x]:
        if visited[one] == 0:
            visited[one] = 1
            q.append(one)
            distance[one] = distance[x] + 1

print(distance[target_b])

