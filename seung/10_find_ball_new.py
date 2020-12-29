import sys
from collections import defaultdict
sys.stdin = open("./seung/input.txt","r")
N,M = map(int,sys.stdin.readline().split())
tmp_lst = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
lighter_node_graph = defaultdict(list)
heavier_node_graph = defaultdict(list)
for i, j in tmp_lst:
        lighter_node_graph[i].append(j)
        lighter_node_graph[j]
        heavier_node_graph[j].append(i)
        heavier_node_graph[i]

median = (N+1)//2
def bfs(vertex,graph):
    global count
    visited_node[vertex] = 1 # 방문 체크 해줘야 함.
    for item in sorted(graph[vertex]):
        if visited_node[item] == 0:
            # visited_node[item] = count
            count += 1
            bfs(item,graph)
    return count
heavy_cnt=0
light_cnt=0
for marble in range(1,N+1):
    visited_node = [0 for _ in range(N + 1)]
    count = 0 # dfs 탐색하는 개수를 무거운거 찾을 때, 가벼운거 찾을 때 각각 초기화
    if bfs(marble,heavier_node_graph) >= median:
        heavy_cnt+=1
    count  = 0
    if bfs(marble,lighter_node_graph) >= median:
        light_cnt+=1

print(heavy_cnt+light_cnt)