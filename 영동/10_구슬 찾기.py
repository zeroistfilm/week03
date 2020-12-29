# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2617

# 중간 값이 될 수 없다 == 현재 구슬보다 무겁거나or가벼운것이 (n+1)/2 보다 많을때
# dfs로 현재 구슬보다 무거운 구슬이 몇개 인지 구한다


def solve():
    global count
    N,M = map(int,input().split())

    light = [[]for i in range(N+1)]
    heavy = [[]for i in range(N+1)]
    for i in range(M):
        a = list(map(int, input().split()))
        light[a[0] - 1].append(a[1] - 1) #주어진 데이터를 이용해 해당 노드보다 가벼운 간선 노드 정보를 넣는다
        heavy[a[1] - 1].append(a[0] - 1) #마찬가지로 무거운 간선 정보를 넣는다

    def dfs(dataset,startnode): #노드를 돌면서 처음 노드에서 도달할 수 있는 노드의 갯수를 구한다.
        global count
        visited[startnode]=True
        for i in dataset[startnode]:
            if visited[i]==False:
                visited[i] = True
                dfs(dataset,i)
                count+=1
    heavylist=[]
    for i in range(N): #해당하는 모든 노드를 돌면서 본인보다 무거운 노드의 갯수를 담는다. 무거운 정보는 인접리스트에서 저장한다.
        visited=[False for i in range(N+1)]
        count=0
        dfs(heavy,i)
        heavylist.append([i,count]) #현재 노드와 본인보다 무거운 노드의 갯수를 리스트에 저장한다.

    lightlist=[]
    for i in range(N):#해당하는 모든 노드를 돌면서 본인보다 가운 노드의 갯수를 담는다. 가벼운 정보는 인접리스트에서 저장한다.
        visited=[False for i in range(N+1)]
        count=0
        dfs(light,i)
        lightlist.append([i,count])#현재 노드와 본인보다 가벼운 노드의 갯수를 리스트에 저장한다.

    result=0
    for i in range(N): #가장핵심적인 부분인데 N개의 노드의 중간은 N+1/2의 인덱스 번호를 가진다.  절대로 중간이 될수 없다는 건 중간 인덱스를 벗어난다는 뜻이다.
        if (N+1)/2<=heavylist[i][1]: #중간인덱스보다 같거나 큰 구슬 개수를 가지면 해당 구슬은 중간이 될 수 없다.
            result+=1
        if (N+1)/2<=lightlist[i][1]:
            result+=1
    print(result)

solve()