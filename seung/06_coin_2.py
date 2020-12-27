import sys
from collections import deque
sys.stdin = open("./seung/input.txt","r")

n, k = map(int,sys.stdin.readline().split())
coin_lst = list(int(sys.stdin.readline()) for _ in range(n))
queue = deque([])
cnt = 1
visited = set() # set으로 고유한 값만 잡음.
visited.update(coin_lst)
for i in range(n):
    queue.append([coin_lst[i],i,cnt])

flag  = True
while queue :
    check_num = queue.popleft()
    cnt = check_num[2] + 1
    for i in range(check_num[1],len(coin_lst)):
        sum = [check_num[0] + coin_lst[i],i, cnt]
        if sum[0] == k:
            print(cnt)
            flag = False
            break
        elif sum[0] > k:
            continue
        if sum[0] not in visited:
            queue.append(sum)
            visited.add(sum[0])
    if not flag:
        break
if flag:
    print(-1)