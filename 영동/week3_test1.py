# https://www.acmicpc.net/problem/2667
import sys
from collections import deque
N = int(sys.stdin.readline())
maps=[[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    tmp = sys.stdin.readline().strip()
    for j in range(len(tmp)):
        maps[i][j] = int(tmp[j])


visited=[[False for _ in range(N)]for _ in range(N)]

def finishcheck(maps):
    countTure=0
    counthouse = 0
    for r in range(N):
        for c in range(N):
            if maps[r][c]!=0:
                counthouse+=1
            if visited[r][c]==True:
                countTure+=1
    if counthouse ==countTure:
        return True
    else:
        return False


def counthouse(maps):
    number=[0]*1000
    for r in range(N):
        for c in range(N):
            if maps[r][c] !=0:
                number[maps[r][c]]+=1
    return number



dr =[0,0,1,-1]
dc =[1,-1,0,0]
def bfs(maps,visited):
    global checkflag

    #방문할 위치 찾기
    flag=False
    for r in range(N):
        for c in range(N):
            if maps[r][c] !=0 and visited[r][c]==False:
                start = [r,c]
                flag=True
                break
        if flag==True:
            break
    if finishcheck(maps)==True: return True
    checkflag += 1
    queue = deque([start])
    visited[start[0]][start[1]] = True
    maps[start[0]][start[1]] = checkflag
    while queue:
        v = queue.popleft()
        for i in range(4):
            nr = v[0]+dr[i]
            nc = v[1]+dc[i]
            if 0<=nr<N and 0<=nc<N and visited[nr][nc]==False and maps[nr][nc]==1:
                queue.append([nr,nc])
                maps[nr][nc]=checkflag
                visited[nr][nc]=True


checkflag=0
while True:
    check = bfs(maps,visited)
    if check==True:
        print(checkflag)
        answer=[x for x in counthouse(maps) if x!=0]
        for i in sorted(answer):
            print(i)
        break

