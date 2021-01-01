#[트리의 지름 문제]
# - A로부터 가장 먼 점 B
# - B로부터 가장 먼점 C
# 두개 합치면 트리의 지름이라는 증명이 있음.  # https://blog.myungwoo.kr/112
#
# 다익스트라 써서 모든 정점의 거리를 구한 다음, 그 중 가장 큰 거리 구함.(bfs로 푸는게 좋을듯. 가장 거리가 작은 정점부터 출발해서 모든 정점까지의 최소거리)
# 구현할 때는 우선순위 큐 쓰면 좋음.

import sys,heapq
sys.stdin = open("./seung/input.txt","r")
n = int(input())
node_info = [list(map(int,sys.stdin.readline().split())) for _ in range(n-1)]
# 인접 리스트를 2차원 배열로 표현. 인덱스 0은 안 쓸거라, 범위는 n+1까지.
ad_graph_array = [[] for i in range(n + 1)]

# ad_graph_Array는 인접리스트를 배열로 만든건데, 부모노드를 배열 인덱스로 하고, 그 부모노드의 자식 노드가 뭐가 있는지 표현. 자식노드가 없으면 빈배열. 인덱스 0은 제외
# 딕셔너리로 만들면 키를 부모 노드, 밸류를 자식 노드하면 되는데/ 리스트로 만들면 인덱스가 부모 노드, 인덱스의 값을 자식 노드로 하면 될듯.
# 리스트 인덱스(부모 노드)를 기준으로 값에 [자식노드, 가중치] 담기
# 문제를 풀려면 단방향이 아니라 양방향이어야 한다.
for node in node_info:
    p,c,w = node
    ad_graph_array[p].append([c, w])
    ad_graph_array[c].append([p,w])

inf = sys.maxsize
def get_distance(ad_graph, start):
    minimum_distance = [inf for i in range(n + 1)]
    minimum_distance[start] = 0
    queue = []
    heapq.heappush(queue, [minimum_distance[start], start])
    while queue:
        acc_distance, position = heapq.heappop(queue)
        for arrival, weight in ad_graph[position]:
            distance = acc_distance + weight
            if minimum_distance[arrival] > distance:
                minimum_distance[arrival] = distance
                heapq.heappush(queue, [distance, arrival])
    return minimum_distance


# 아무 노드 부터 시작해서 제일 먼 점 찾으면 되긴함. 근데 루트노드인 1부터 시작해보자.
min_d_list = get_distance(ad_graph_array, 1)
# 먼 점을 찾고 나서 그 점에서 먼 점을 또 찾자.(다익스트라 한번 더 돌린 다음 거기에서 최대 고르기)
# 인덱스 0은 어짜피 안 쓰니까 제외.
max_d_index = min_d_list.index(max(min_d_list[1:]))
min_d_list2 = get_distance(ad_graph_array,max_d_index)

print(max(min_d_list2[1:]))