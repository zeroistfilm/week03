import sys
from collections import defaultdict,deque
sys.stdin = open("./seung/input.txt","r")
N,M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
tmp_lst = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
incoming_degree = [0 for i in range(N + 1)] # 전입차수 리스트 미리 만들어놓기
queue = deque([])
result = []

# 전입차수 리스트,인접 그래프 만들기
for i, j in tmp_lst: # from과 to 중에 to로 들어오는 수가 전입차수이니까 j인 것을 +1한다.
    graph[i].append(j)
    graph[j]
    incoming_degree[j] += 1

# 첫 큐를 만든다. 전입차수가 0인 애들은 큐에 넣는다.
for i in range(1, N+1):
    if incoming_degree[i] == 0:
        queue.append(i)
# 큐에 넣고 위상정렬을 돌린다.
while queue:
    tmp = queue.popleft()
    result.append(tmp)
    for j in graph[tmp]: # 그 정점의 인접리스트에 해당하는 지점들(진입차수가 있는 점)을 확인한다.
        incoming_degree[j] -= 1 # 큐에서 하나 빼고 그거와 연관된 간선은 빼준다.
        if incoming_degree[j] == 0: # 진입차수가 0인 정점들은 큐에 넣는다.
            queue.append(j)

print(*result)