import sys
from collections import deque
sys.stdin = open("./seung/input.txt","r")

n, k = map(int,sys.stdin.readline().split())
coin_lst = list(int(sys.stdin.readline()) for _ in range(n))
queue = deque([])
visited = [0 for _ in range(100001)]
for i in range(len(coin_lst)):
    queue.append([coin_lst[i],i,0])
flag = False
while queue:
    item, i,cnt = queue.popleft()
    cnt += 1
    if item == k:
        flag = True
        print(cnt)
        break
    elif item > k:
        continue

    for index in range(i, len(coin_lst)):
        sum = coin_lst[index] + item
        if visited[sum] == 0:
            queue.append([sum,index,cnt])
            visited[sum] = 1


if not flag :
    print(-1)