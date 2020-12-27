import sys
from collections import defaultdict
# sys.setrecursionlimit(10 ** 9)
sys.stdin = open("./seung/input.txt","r")
n = int(sys.stdin.readline())
tmp_lst = [list(map(int,sys.stdin.readline().split())) for _ in range(n-1)]
graph = defaultdict(list)
for i, j in tmp_lst:
        graph[i].append(j)
        graph[j].append(i)

parent_node = [ 0 for _ in range(n+1)] # 방문한 노드의 부모 노드를 찍기 위한 배열 생성(편리한 인덱스를 위해 0~N까지). 밑에서 탐색한 item의 부모 노드를 찍었다는건, 이미 방문한거니까 또 방문 안해도 됨.
def recursive_dfs(vertex):
    for item in sorted(graph[vertex]):
        if parent_node[item] == 0: # 방문 확인 리스트에서 item을 'in'으로 탐색하면 O(N) 걸림. N이 100000개이면 시간초과가 남. 미리 리스트를 만들고 그 리스트의 인덱스 확인은 O(1)일듯.
            parent_node[item] = vertex # 부모 노드를 리스트에 저장
            recursive_dfs(item)

recursive_dfs(1)
for i in range(2,n+1): #2번인덱스(2번 노드)부터 출력하면 됨.
    print(parent_node[i])