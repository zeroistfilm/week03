import sys
sys.stdin = open("./seung/input.txt","r")
import collections

# sys.stdin = open('BOJ2667.txt')
N, K = list(map(int,sys.stdin.readline().split()))
board = []
path = []
ans = []
que = collections.deque([])
result = []
que.append([N,N])

def bfs():
    pn, n = que.popleft()
    visited = [False] * N

    que.append(n)
    while len(que) != 0:
        pn ,n = que.popleft()
        if 0 <= n <= 100000 and not visited[n][1]:
            visited[n][0] = abs(n-pn)+visited[pn]
            visited[n][1] = True
            if n == K:
                print(visited[n][0])
                result.append(visited[n])

            else:
                    que.append([n ,2*n])
                    que.append([n ,n+1])
                    que.append([n ,n-1])

bfs()
