# https://www.acmicpc.net/problem/1987
import sys

R, C = map(int, sys.stdin.readline().split())
map = [list(map(lambda x: ord(x) - 65, sys.stdin.readline().rstrip())) for _ in range(R)]  # 아스키코드 값으로 전부 변환해서 저장'

visited=[0]*26
visited[map[0][0]] = 1
dr= [1, -1, 0, 0]
dc= [0, 0, 1, -1]
answer = 1


def dfs(r, c, count):
    global answer
    answer = max(answer, count)
    for i in range(4):
        new_row = r + dr[i]
        new_col = c + dc[i]
        if 0 <= new_row < R and 0 <= new_col < C:
            if visited[map[new_row][new_col]] == 0:
                visited[map[new_row][new_col]] = 1
                dfs(new_row, new_col, count+1)
                visited[map[new_row][new_col]] = 0

dfs(0, 0, answer)
print(answer)



