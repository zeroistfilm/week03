import sys
from collections import deque
read = sys.stdin.readline

n, k = map(int, read().split())
coin = deque()
for _ in range(n):
    coin.append(int(read()))

