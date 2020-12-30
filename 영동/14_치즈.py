# https://www.acmicpc.net/problem/2638
import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for i in range(R)]

dr=[0,0,1,-1]
dc=[1,-1,0,0]
def pro():
    def bfs(map, start, visited):
        queue = deque([start])
        visited[start[0]][start[1]]=True
        while queue:
            air = queue.popleft()
            for i in range(len(dr)):
                nr = air[0] + dr[i]
                nc = air[1] + dc[i]
                if 0<= nr < R and 0<= nc < C and visited[nr][nc]==False:
                    if map[nr][nc]==0:
                        queue.append([nr,nc])
                        map[nr][nc]=0
                        visited[nr][nc]=True
                        for i in range(len(dr)):
                            nnr = nr + dr[i]
                            nnc = nc + dc[i]
                            if 0 <= nnr < R and 0 <= nnc < C and map[nnr][nnc] == 1:
                                if visited[nnr][nnc] == False:
                                    visited[nnr][nnc] = True
                                else:
                                    map[nnr][nnc]-=1

    def finalcheck(map):
        result=0
        for r in range(len(map)):
            result += sum(map[r])
        return result/len(map[1])

    time=0
    while True:
        visited = [[False for _ in range(C)] for _ in range(R)]
        bfs(map,[0,0],visited)
        time+=1
        if finalcheck(map)==0:
            print(time)
            break
pro()