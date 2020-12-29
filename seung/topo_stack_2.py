from collections import defaultdict
adj_list = [[0,2], [0,3],[1,3],[1,4],[2,3],[3,5],[2,5],[4,5]]
# adj_list = {0: [2, 3], 1: [3, 4], 2: [3, 5], 3: [5], 4: [5], 5: []}
graph = defaultdict(list)
def topological_sort_stack(adj_list):
    stack = []
    incoming_degree = [0] * 6
    answer = []

    for i, j in adj_list:
        graph[i].append(j)
        graph[j]
        incoming_degree[j] += 1

    for index in range(len(incoming_degree)):
        if incoming_degree[index] == 0:
            stack.append(index)

    while stack:
        node = stack.pop()
        answer.append(node)

        for graph_key_len_i in range(len(graph[node])): # 인접 그래프의 키 값(리스트)의 길이만큼 인덱스 뽑기
            idx = graph[node][graph_key_len_i] # idx = 인접 그래프의 키에 해당하는 밸류의 순서
            incoming_degree[idx] -= 1 # 그 순서에 해당하는 진입차수 배열에서 진입차수를 -1한다. (ex. 노드 3의 진입차수를 -1하라)
            if incoming_degree[idx] == 0: # -1해서 0이 됐으면 그 노드를 스택에 담아라.
                stack.append(idx)

    print(answer)


topological_sort_stack(adj_list)
