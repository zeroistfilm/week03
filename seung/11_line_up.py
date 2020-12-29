import sys
from collections import deque,defaultdict
sys.stdin = open("./seung/input.txt","r")
N,M = map(int,sys.stdin.readline().split())
tmp_lst = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
#인접 리스트 구하기
graph = defaultdict(list)
for i, j in tmp_lst:
        graph[i].append(j)
        graph[j]


que = deque([])
incoming_degree = [0] * (len(graph)+1)
answer = []
print("진입차수 계산 전 :",incoming_degree)
# 진입차수 계산해서 세팅해주기
for i in range(len(graph)):
    for j in range(len(graph)):
        temp = graph[j]
        for k in range(len(temp)):
            if temp[k] == i:
                incoming_degree[i] += 1
print("진입차수 계산 후 :",incoming_degree)

# 진입차수가 0인 원소들부터 큐에 넣기
for i in range(1,len(incoming_degree)):
    if incoming_degree[i] == 0:
        que.append(i)

while que: #큐에 원소가 있을 때까지
    node = que.popleft()
    answer.append(node)
    print("답: ",answer)
    for i in range(len(graph[node])):
        idx = graph[node][i]
        incoming_degree[idx] -= 1
        if incoming_degree[idx] == 0:
            que.append(idx)
    print("진입차수 큐 안에서", incoming_degree)
print(*answer)
