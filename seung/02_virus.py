import sys
from collections import defaultdict,deque
sys.stdin = open("./seung/input.txt","r")
com_num,pair_num = int(sys.stdin.readline().strip()), int(sys.stdin.readline().strip())

tmp_lst = sorted([list(map(int,sys.stdin.readline().split())) for _ in range(pair_num)])

# 인접 간선 정하기
graph = defaultdict(list)
for i, j in tmp_lst:
        graph[i].append(j)
        graph[j].append(i)

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

print(len(bfs(1))-1)