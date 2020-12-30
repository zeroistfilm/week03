# https://www.acmicpc.net/problem/2636
import sys

R, C = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for i in range(R)]
def pro():


    visited = [[False for _ in range(C)]for _ in range(R)]

    dr=[0,0,1,-1]
    dc=[1,-1,0,0]

    def bfs(map, start, visited):
        from collections import deque

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
                            if 0 <= nnr < R and 0 <= nnc < C and visited[nnr][nnc] == False:
                                if map[nnr][nnc] == 1:
                                    map[nnr][nnc]-=1
                                    visited[nnr][nnc]=True

    def finalcheck(map):
        result=0
        for r in range(len(map)):
            result += sum(map[r])
        return result/len(map[1])

    def checkPiece(map):
        result = 0
        for r in range(len(map)):
            for c in range(len(map[1])):
                if map[r][c]==1:
                    result+=1
        return result
    time=0
    CeckP= checkPiece(map)
    if CeckP==0:
        print(time)
        print(CeckP)
    else:
        while True:
            time += 1
            bfs(map,[0,0],visited)
            if finalcheck(map) == 0:
                print(time)
                print(CeckP)
                break
            visited = [[False for _ in range(C)] for _ in range(R)]
            CeckP= checkPiece(map)
pro()