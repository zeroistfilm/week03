import sys
from collections import deque
read = sys.stdin.readline

n, k = map(int, read().split())
arr = [-1] * 200001
queue = deque()
queue.append(n)
arr[n] = 0
while queue:
    x = queue.popleft()
    for i in [1, -1, x]:
        new = x + i
        if new < 0 or new > 200000: continue
        if arr[new] == -1:
            arr[new] = arr[x] + 1
            queue.append(new)

print(arr[k])