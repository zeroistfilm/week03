# https://www.acmicpc.net/problem/2637
from collections import deque, defaultdict
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
manual = [[]for i in range(N)]
indegree= [[]for i in range(N)]
for i in range(M):
    x,y,k = map(int,sys.stdin.readline().split())
    for i in range(k):
        manual[x-1].append(y-1)
        indegree[y-1].append(x-1)

base=defaultdict(int)

for i in range(len(manual)):
    if len(manual[i])==0: #기본부품
       base[i]=0

def topology():
    queue=deque()
    for i in range(N):
        if len(indegree[i])==0:
            queue.append(i)
    while queue:
        now = queue.popleft()
        if manual[now] == []:
            base[now]+=1
            #print(now, '는 기본부품입니다.')
        for i in manual[now]:
                queue.append(i)

topology()

for k, values in base.items():
    print(k+1,values)
