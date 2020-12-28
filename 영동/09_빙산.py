# https://www.acmicpc.net/problem/2573
import sys
sys.setrecursionlimit(10**9) #런타임 에러 방지
N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]


def melting_dfs(map, start, visited):
    global cntfalse
    visited[start[0]][start[1]] = True
    row = start[0]
    col = start[1]
    cntfalse -= 1
    for i in range(4):
        nrow = row + drow[i]
        ncol = col + dcol[i]
        if 0 <= nrow < N and 0 <= ncol < M and map[nrow][ncol] !=0:#빙산 녹이기
            map[nrow][ncol]-=1
        if 0 <= nrow < N and 0 <= ncol < M and visited[nrow][ncol] == False:
            visited[nrow][ncol] == True
            melting_dfs(map,[nrow,ncol],visited)
            visited[nrow][ncol] == False

def year_meltingcycle(maps,visited):
    for i in range(N):
        for j in range(M):
            if visited[i][j] == False:
                start = [i, j]
                breaker = True
                break
        if breaker == True:
            breaker=False
            break
    # 출발지 정하는것도 해야함
    while cntfalse>0: #1년 싸이
        melting_dfs(maps, start, visited)
        if cntfalse ==0:
            break
        else:
            for i in range(N):
                for j in range(M):
                    if visited[i][j]==False:
                        start=[i,j]
                        breaker = True
                        break
                if breaker==True:
                    breaker == False
                    break

def counting_dfs(map,start,visited):
    global cntfalse
    visited[start[0]][start[1]] = True
    row = start[0]
    col = start[1]
    cntfalse -= 1
    for i in range(4):
        nrow = row + drow[i]
        ncol = col + dcol[i]
        if 0 <= nrow < N and 0 <= ncol < M and visited[nrow][ncol] == False:
            visited[nrow][ncol] == True
            counting_dfs(map, [nrow, ncol], visited)
            visited[nrow][ncol] == False


def count_land(maps,visited):
    global cntfalse,year_count
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 0:
                visited[i][j] = False
                cntfalse+=1
                start = [i, j]
    counting_dfs(maps,start,visited)
    if cntfalse ==0:
        return True #('한덩어리입니당')
        year_count += 1
    else:
        year_count += 1
        return False

check=True
year_count=1
while check==True:
    cntfalse = N * M
    visited = [[False for _ in range(M)] for _ in range(N)]
    #visited초기화
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 0:
                visited[i][j] = True
                cntfalse -= 1
    year_meltingcycle(maps,visited)
    check =count_land(maps,visited)
print(year_count)
