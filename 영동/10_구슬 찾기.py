# https://www.acmicpc.net/problem/2617
N,M = map(int,input().split())

adjList1 = [[] for i in range(N)]
adjList2 = [[] for i in range(N)]
for i in range(M):
    a = sorted(list(map(int, input().split())))
    adjList1[a[0] - 1].append(a[1] - 1)
    adjList2[a[1] - 1].append(a[0] - 1)


count=0
for i in range(len(adjList1)):
    if len(adjList1[i])>=2:
        count+=1
    if len(adjList2[i]) >= 2:
        count += 1
print(count)