

from collections import deque
N,K = map(int, input().split())
Max=10**5+1
queue=deque([N])
D=[[-1]*2 for _ in range(Max)]
D[N][0]=0
T=[K]
z=K

while queue:
    v = queue.popleft()
    for newv in [v-1,v+1,v*2]:
        if 0<= newv < Max and D[newv][0]==-1:
            queue.append(newv)
            D[newv][0]=D[v][0]+1
            D[newv][1]=v

while D[z][1]!=-1:
    T.append(D[z][1])
    z=D[z][1]
print(D[K][0])
print(*reversed(T))