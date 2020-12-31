import sys
from collections import deque, defaultdict
read = sys.stdin.readline

n, k = map(int, read().split())
arr = [-1] * 200001
queue = deque()
queue.append(n)
arr[n] = 0
parent = defaultdict(int)
cnt = 0

if n == k:
    print(0)
    print(n)
    exit()

while queue:
    x = queue.popleft()
    # print(x, end=' ')
    if x == k: break
    for i in [1, -1, x]:
        new = x + i
        if new < 0 or new > 200000: continue
        if arr[new] == -1:
            arr[new] = arr[x] + 1
            parent[new] = x
            queue.append(new)

print(arr[k])
result = [str(k)]
while True:
    start = k
    if parent[k] == n: break
    result.append(str(parent[k]))
    k = parent[k]

print(n, end=' ')
print(' '.join(result[::-1]))
