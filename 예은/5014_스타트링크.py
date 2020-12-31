import sys
from collections import deque
read = sys.stdin.readline

def solve():
    total, start, end, up, down = map(int, read().split())

    # 첫 번째 풀이 (배열 잡아서 품, 근데 이게 더 메모리 적음 ;; )
    howmany = [-1] * 2000001
    howmany[start] = 0

    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        if now == end:
            return howmany[now]
        if now + up <= total and howmany[now+up] == -1:
            howmany[now+up] = howmany[now] + 1
            q.append(now+up)
        if now - down >= 1 and howmany[now-down] == -1:
            howmany[now-down] = howmany[now] + 1
            q.append(now-down)

    return "use the stairs"

    # 두번째 풀이 (방문체크에 set이용)
    # q = deque()
    # q.append([start, 0])
    # visited = {start}
    # while q:
    #     now, cnt = q.popleft()
    #     if now == end:
    #         return cnt
    #     if now + up <= total and (now+up) not in visited:
    #         visited.add(now+up)
    #         q.append([now+up, cnt+1])
    #     if now - down >= 1 and (now-down) not in visited:
    #         visited.add(now-down)
    #         q.append([now - down, cnt+1])
    #
    # return "use the stairs"

print(solve())


