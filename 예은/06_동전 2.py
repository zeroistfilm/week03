import sys
from collections import deque
read = sys.stdin.readline

# dp
# n, k = map(int, read().split())
# coins = []
# for _ in range(n):
#     coins.append(int(read()))
#
# coins.sort()
# dp = [10001] * (k+1)
# dp[0] = 0
# for i in range(1, k+1):
#     for coin in coins:
#         if i - coin < 0 : break
#         dp[i] = min(dp[i], dp[i - coin] + 1)
#
# print(-1 if dp[k] == 10001 else dp[k])

# bfs
n, k = map(int, read().split())
coins = sorted(list(set(int(read()) for _ in range(n)))) # 같은 동전 있으니까 set
visited = [0 for _ in range(100001)] # 방문 확인
q = deque()
for coin in coins:
    q.append([coin, 1]) # 코인값, 개수  큐에 넣어줌
    visited[coin] = 1

flag = False # 다돌고도 불가능하면 -1 출력용
while q:
    value, cnt = q.popleft()
    if value == k:
        flag = True
        print(cnt)
        break

    for coin in coins:
        if value + coin > k : break # 크기순 정렬해뒀으니까 커지면 바로 break
        if not visited[value + coin]:
            q.append([value + coin, cnt + 1])
            visited[value + coin] = 1

if not flag:
    print(-1)