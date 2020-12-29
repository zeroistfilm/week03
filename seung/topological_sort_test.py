# Python program to print topological sorting of a DAG
from collections import defaultdict


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # 정점(꼭지점) 개수

    # function to add an edge to graph
    def addEdge(self, from_v, to_v):
        self.graph[from_v].append(to_v)

        # A recursive function used by topologicalSort

    def topologicalSortUtil(self, vertex, visited, stack):

        # Mark the current node as visited.
        visited[vertex] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[vertex]:
            if visited[i] == False: #아직 방문 안했으면, 재귀 호출
                self.topologicalSortUtil(i, visited, stack)

                # Push current vertex to stack which stores result
        stack.insert(0, vertex) #근데 왜 0을 고정시킬까?

        # The function to do Topological Sort. It uses recursive

    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V): # 정점 개수만큼 반복문 수행
            if visited[i] == False: #아직 방문 안한 정점이면, 위상정렬 함수 실행
                self.topologicalSortUtil(i, visited, stack)
        print(stack)


g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

print("Following is a Topological Sort of the given graph")
g.topologicalSort()
