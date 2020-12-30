# https://www.acmicpc.net/problem/19236

import sys
from collections import deque
sea=[[]for i in range(4)]
for i in range(4):
    temp = list(map(int,input().split()))
    for j in range(4):
        sea[i].append([temp[2*j],temp[2*j+1]])

# def fishsort(sea):
#     sortedfish=[]
#     for i in range(4):
#         for j in range(4):
#             sortedfish.append([i,j,sea[i][j]])
#     sortedfish.sort(key=lambda x:x[2])
#     sortedfish = deque(sortedfish)
#     return sortedfish

visited = [[False for _ in range(4)] for _ in range(4)]
dr = [-1, -1,  0,  1,  1,  1,  0, -1,-1, -1,  0,  1, 1, 1, 0, -1]
dc = [ 0, -1, -1, -1,  0,  1,  1,  1, 0, -1, -1, -1, 0, 1, 1,  1]
#####  ↑,  ↖,  ←,  ↙,  ↓,  ↘,  →,  ↗, ↑,  ↖,  ←,  ↙, ↓, ↘, →,  ↗

def find_fish(index):
    for r in range(4):
        for c in range(4):
            if sea[r][c][0]==index:
                return [r,c]
    return False

def fish_move(sea):

    for i in range(16):
        position=find_fish(i+1)
        if position ==False:
            continue
        else:
            r=position[0]
            c=position[1]
        if sea[r][c] ==-1:
            break
        for i in range(8):
            nr = r + dr[sea[r][c][1]-1+i]
            nc = c + dc[sea[r][c][1]-1+i]
            if 0<=nr<4 and 0<=nc<4 and sea[nr][nc][0]!=-1:
                sea[r][c],sea[nr][nc]=sea[nr][nc],sea[r][c]
                break

sea[0][0] = [-1,sea[0][0][1]]
fish_move(sea)
print('a')