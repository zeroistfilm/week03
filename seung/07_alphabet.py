import sys
sys.setrecursionlimit(10 ** 9)
sys.stdin = open("./seung/input.txt","r")
ROW,COL = map(int,sys.stdin.readline().split())
matrix= [ list(sys.stdin.readline().strip()) for _ in range(ROW)]

dx = [-1,0,1,0] # 순서대로 좌, 상, 우, 하
dy = [0,1,0,-1]

count = 1
def solve():
        # 재귀로 풀려면 좌표를 줘야 함.
        def dfs(x,y,cnt):
            global count
            # count = cnt
            count = max(cnt,count) #왜 이거 매번할까?
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                # 바깥에 나가거나 visited에 있는 알파벳이면 가면 안 됨.
                if 0<= next_x < ROW and 0 <= next_y < COL and matrix[next_x][next_y] not in visited:
                    visited.add(matrix[next_x][next_y])
                    dfs(next_x,next_y,cnt+1) # 4방향으로 재귀호출해서 타고 들어가기
                    visited.remove(matrix[next_x][next_y]) # 백트래킹이 된거면 visited 배열에서 다녀왔던 알파벳 빼기(다시 다른데 가야하니까)
        dfs(0,0,count)
start_vertex = matrix[0][0]
visited = set(start_vertex)
solve()
print(count)