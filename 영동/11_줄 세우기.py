# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2252

from collections import deque

V,E = map(int ,input().split())

approch=[[]for i in range(V)]
link=[[]for i in range(V)]

for i in range(E):
    a,b  = map(int,input().split())
    approch[b-1].append(a-1) #집입차수
    link[a - 1].append(b - 1)  #간선 정보

queue = deque()
visited=[False for i in range(V)]
접근순서 =[]
def topology(approch,link,visited):
    for _ in range(V):
        for i in range(V):#모든 노드를 돌면서 진입차수가 0인 노드를 모두 집어 넣는다
            if len(approch[i])==0 and visited[i]==False:
                queue.append(i) # 노드 번호를 큐에 집어 넣는다
                접근순서.append(i)
                visited[i]=True

        while queue:
            popv = queue.popleft()
            c=link[popv]
            for j in range(len(link[popv])):
                approch[link[popv][j]]=[] #간정 정보를 비운다

topology(approch,link,visited)
for i in range(len(접근순서)):
    print(접근순서[i]+1,end=' ')
