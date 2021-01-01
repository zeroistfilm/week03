import heapq
mycountry = {
    'A': {'B':8, 'C':1,'D':2},
    'B': {},
    'C': {'B':5, 'D':2},
    'D': {'E':3,'F':5},
    'E': {'F':1},
    'F': {'A':5}
}

def digkstra(ad_graph,start):
    minimum_distance = {node:float('inf') for node in ad_graph}
    minimum_distance[start]= 0

    queue = []
    # 큐에 출발점이 갈 수 있는 거리 세트, 출발점을 같이 넣어줌.
    heapq.heappush(queue, [minimum_distance[start],start])

    while queue:
        print("----")
        print("큐 : ",queue)
        # 각각 minimum_distance[start],start 라고 보면 됨. 예를 들어서 0, A가 나올 수 있음.
        current_d, position = heapq.heappop(queue)
        print("current_d, position:",current_d,position)
        # 현재 minimum distacne 상의 position에 찍혀있는 거리가 누적거리(current_d)보다 작으면 아예 스킵. 이미 F에 6이 찍혀있는데, 큐에서 뽑은 거리가 7이면 볼 필요 없음.
        print("minimum 배열, 값:", minimum_distance, minimum_distance[position])
        if minimum_distance[position] < current_d:
            continue
        # 예를 들어 A의 value를 꺼내면 arrival은 B, weight는 8
        for arrival, weight in ad_graph[position].items():
            print("arrival,weight:", arrival, weight)
            distance = current_d + weight # 예를 들어 0과 8을 더해서 8을 구한다.
            print("distance:", distance)
            # 기존 거리보다 distance가 더 작으면 교체해줌. arrival이 B이면 inf가 나온다. inf가 8(distance)보다 더 작은지 비교
            if distance < minimum_distance[arrival]:
                minimum_distance[arrival] = distance
                # 새로운 점에서 출발해야 하니까 arrival과 그점까지의 누적 거리(distance)을 큐에 넣음.
                heapq.heappush(queue, [distance,arrival])
    return minimum_distance

print(digkstra(mycountry,'A'))
