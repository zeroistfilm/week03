from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def helper(self, v, visited, stack): # Sort 함수에서 순차적으로 반복문 돌 때의 인덱스를 v로 받음.

        visited[v] = True # 그 정점은 이미 도달했으니 방문으로 추가

        for i in self.graph[v]: # 그 지점에서 더 타고 들어갈 수 있는게 있는지 확인(DFS)
            if visited[i] == False: # 방문 안한거면 더 타고 들어가게 재귀 호출
                self.helper(i, visited, stack)

        stack.append(v) #재귀 끝나면 끝난 순서대로 스택에 추가

    def topologicalSort(self):

        visited = [False] * self.V
        stack = []

        for i in range(self.V): # 정점 수만큼(ex. 1~5) 반복문 돈다. 순차적으로 반복문을 돌리면서 방문을 안했으면(보통 첫 방문일 것인데, 어떤 정점의 화살표 끝에 이미 방문한 지점들이 있을 순 있다.)재귀함수 실행
            if visited[i] == False:
                self.helper(i, visited, stack)

        while stack:
            print(stack.pop())

g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
print(g.graph)
print("Following is a Topological Sort of the given graph")
g.topologicalSort()