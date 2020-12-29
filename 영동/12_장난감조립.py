# https://www.acmicpc.net/problem/2637

from collections import deque, defaultdict
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

need_part = [[] for i in range(N)]
parts_needed = [0 for _ in range(N)]
EA = [0 for _ in range(N)]
visited = [False for _ in range(N)]
basic=[]

for i in range(M):
    x,y,ea = map(int, input().split())
    need_part[x-1].append([y-1,ea])
    parts_needed[y-1]+=1

while sum(parts_needed)>0:
    for i in range(N):
        if not need_part[i] and visited[i] ==False:
            basic.append(i)
            visited[i] = True
        if parts_needed[i]==0 and visited[i] ==False:
            if EA[i]==0:
                EA[i]=1
            visited[i]=True

            for j in need_part[i]:
                EA[j[0]]+=j[1]*EA[i]
                parts_needed[j[0]]-=1


for i in basic:
    print(i+1, EA[i], sep=" ")