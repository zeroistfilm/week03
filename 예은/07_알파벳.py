import sys
read = sys.stdin.readline

r, c = map(int, read().split())
field = [list(map(lambda x: ord(x)-65, read().rstrip())) for _ in range(c)] # 아스키코드 값으로 전부 변환해서 저장

visited = [0] * 26
visited[field[0][0]] = 1
drow = [1, -1, 0, 0]
dcol = [0, 0, 1, -1]
answer = 1

# dfs 풀이,런타임에러 ?
def dfs(row, col, cnt):
    global answer
    answer = max(answer, cnt)
    for i in range(4):
        new_row = row + drow[i]
        new_col = col + dcol[i]
        if 0 <= new_row < r and 0 <= new_col < c:
            if visited[field[new_row][new_col]] == 0:
                visited[field[new_row][new_col]] = 1
                dfs(new_row, new_col, cnt+1)
                visited[field[new_row][new_col]] = 0


dfs(0, 0, answer)
print(answer)


# bfs 풀이, set 이용, 통과
# set에서 pop하면 랜덤한 원소를 꺼내준다
# def bfs(row, col, answer):
#     queue = set()
#     queue.add((row, col, field[row][col]))
#     while queue:
#         row, col, alpha = queue.pop()
#         answer = max(answer, len(alpha))
#         for i in range(4):
#                 new_row = row + drow[i]
#                 new_col = col + dcol[i]
#                 if 0 <= new_row < r and 0 <= new_col < c and field[new_row][new_col] not in alpha:
#                     queue.add((new_row, new_col, alpha + field[new_row][new_col]))
#     return answer

# print(bfs(0,0,answer))


# 5 5
# IEFCJ
# FHFKC
# FFALF
# HFGCF
# HMCHH
# 10