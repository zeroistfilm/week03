import sys
# sys.stdin = open("./seung/input.txt","r")
ROW,COL = map(int,sys.stdin.readline().split())
matrix= [ list(sys.stdin.readline().strip()) for _ in range(ROW)]

dx = [-1,0,1,0] # 순서대로 좌, 상, 우, 하
dy = [0,1,0,-1]

count = 1

# 재귀로 풀려면 좌표를 줘야 함.
def dfs(x,y,cnt):
    global count
    count = max(cnt,count) #왜 이거 매번할까?
    # stack = [[x,y,matrix[x][y]]]
    # while stack:
    #     x,y = stack.pop()
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        # 바깥에 나가거나 visited에 있는 알파벳이면 가면 안 됨.
        if 0<= next_x < ROW and 0 <= next_y < COL and matrix[next_x][next_y] not in visited:
            visited.append(matrix[next_x][next_y])
            dfs(next_x,next_y,cnt+1) # 4방향으로 재귀호출해서 타고 들어가기
            visited.remove(matrix[next_x][next_y]) # 백트래킹이 된거면 visited 배열에서 다녀왔던 알파벳 빼기(다시 다른데 가야하니까)
        # 아직 안 지나온 알파벳이면 스택에 넣기
        # if matrix[next_x][next_y] not in visited:
        # stack.append([next_x,next_y])
        # count+=1

start_vertex = matrix[0][0]
visited = [start_vertex]
dfs(0,0,count)
print(count)

