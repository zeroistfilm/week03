# https://www.acmicpc.net/problem/2294

# 구하고자 하는 값을 넘어서는 코인은 넣지 않음.
# 코인을 내림차순으로 정렬

from collections import deque
n,k = map(int,input().split())

coins=set()

for i in range(n):
    tmp = int(input())
    if tmp<=k:
        coins.add(tmp)


coins = sorted(list(coins), reverse=True)
visited = set()
visited.update(coins)
queue = deque(coins)

count=0
sucess = False
while queue and not sucess:
    count +=1
    for i in range(len(queue)):
        cost = queue.popleft()
        if cost== k:
            sucess = True
            queue=None
            break
        else:
            for c in coins:
                if cost+c <=k and cost+c not in visited:
                    visited.add(cost+c)
                    queue.append(cost+c)
if sucess:
    print(count)
else:
    print(-1)
