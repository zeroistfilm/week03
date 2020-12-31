# https://www.acmicpc.net/problem/1697
import sys
from collections import deque
N,K = map(int, sys.stdin.readline().split())
Max=10**5+1
queue=deque([N])
D=[[-1]*2 for _ in range(Max)]
D[N][0]=0
while queue:
    v = queue.popleft()
    for newv in [v-1,v+1,v*2]:
        if 0<= newv < Max and D[newv][0]==-1:
            queue.append(newv)
            D[newv][0]=D[v][0]+1 #1초후 정보를 입력
            D[newv][1]=v #위치 입력
print(D[K][0]) #K번째 시간 출력
