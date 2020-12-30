import sys
sys.setrecursionlimit(10**8)
read = sys.stdin.readline

def dfs(graph, x, y):
    if x < 0 or x >= len(field[0]) or y < 0 or y >= len(field):
        return 0
    elif graph[y][x]:
        graph[y][x] = 0
        dfs(graph, x - 1, y)
        dfs(graph, x + 1, y)
        dfs(graph, x, y + 1)
        dfs(graph, x, y - 1)


t = int(read())
for _ in range(t):
    x, y, baechu = map(int, read().split())
    field = [[0] * x for _ in range(y)]
    # 배추밭 상태 입력받기
    for _ in range(baechu):
        baechu_x, baechu_y = map(int, read().split())
        field[baechu_y][baechu_x] = 1
    worm = 0
    for i in range(y):
        for j in range(x):
            if field[i][j]:
                dfs(field, j, i)
                worm += 1
    print(worm)
