# https://www.acmicpc.net/problem/2637

from collections import deque, defaultdict
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

need_part = [[] for i in range(N)]
indeg = [0 for _ in range(N)]
EA = [0 for _ in range(N)]
visited = [False for _ in range(N)]
basic=[]

for i in range(M):
    x,y,ea = map(int, input().split())  #  "중간 부품이나 완제품 X를 만드는데 중간 부품 혹은 기본 부품 Y가 K개 필요하다"
    need_part[x-1].append([y-1,ea]) #인접리스트를 만든다. 방향성이 있음.
    indeg[y-1]+=1 #진입차수를 계산한다.

while sum(indeg)>0:
    for i in range(N):
        if not need_part[i] and visited[i] ==False: #기본 부품은따로 저장한다.
            basic.append(i)
            visited[i] = True
        if indeg[i]==0 and visited[i] ==False: #진입차수가 0인것부터 돈다.
            if EA[i]==0:
                EA[i]=1
            visited[i]=True

            for j in need_part[i]:
                EA[j[0]]+=j[1]*EA[i]
                indeg[j[0]]-=1

for i in basic:
    print(i+1, EA[i], sep=" ")