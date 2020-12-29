import sys
from collections import defaultdict
sys.stdin = open("./seung/input.txt","r")
N,M = map(int,sys.stdin.readline().split())
tmp_lst = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
graph = defaultdict(list)
for i, j in tmp_lst:
        graph[i].append(j)
        graph[j]

median = (N+1)//2
heavier_node = [ set() for _ in range(N+1)]
visited_node = [ 0 for _ in range(N+1) ]
def recursive_dfs(vertex,count,graph):
    global marble
    tmp = marble
    if count > 1:
        heavier_node[vertex].add(tmp)
    for item in sorted(graph[vertex]):
        if visited_node[item] == 0:
            count += 1
            visited_node[item] = count
            # heavier_node[item].add(vertex) # 부모 노드 혹은 조부모 노드들을 set에 계속 저장
            recursive_dfs(item,count,graph)
    # print("count:",count)
for marble in range(1,N+1):
    cnt = 0
    recursive_dfs(marble,cnt,graph)


lighter_node = [set() for _ in range(N+1)]

# print("무거운 순:",)
# print("가벼운 순:",lighter_node)
print("방문:",visited_node)

for num in range(1,N+1):
    for i in range(1,N+1):
        if num in heavier_node[i]:
            lighter_node[num].add(i)
count=0
for node in heavier_node:
    if len(node) >= median:
        count+=1
for node in lighter_node:
    if len(node) >= median:
        count+=1

print(count)