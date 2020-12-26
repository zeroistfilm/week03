import sys
from collections import defaultdict,deque
sys.stdin = open("./seung/input.txt","r")
N,M,V = map(int,sys.stdin.readline().split())
tmp_lst = sorted([list(map(int,sys.stdin.readline().split())) for _ in range(M)])
# 인접 간선 정하기
graph = defaultdict(list)
for i, j in tmp_lst:
        graph[i].append(j)
        graph[j].append(i)
# DFS 구현
def dfs(vertex, visited=[]):
    visited.append(vertex)
    for item in sorted(graph[vertex]):
        # 이전에 방문했던 건 방문하면 안되고, 정점번호가 작은 것을 먼저 방문해야 함.(근데 이미 딕셔너리의 값을 정렬해놨기 때문에 순차적으로 작은거부터 체크 될 것)
        if item not in visited:
            visited = dfs(item, visited)
    return visited

def bfs(start):
    visited= [start]
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        for item in sorted(graph[vertex]):
            if item not in visited: # 이전에 방문했던거 방문하면 안 됨.
                visited.append(item)
                queue.append(item)
    return visited

print(*dfs(V))
print(*bfs(V))