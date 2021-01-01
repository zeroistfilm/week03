import sys
sys.stdin = open("./seung/input.txt","r")
N = int(sys.stdin.readline())
matrix = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

# dfs를 통해 탐색
def danji_dfs(matrix,i,j):
    global unit_danji
    if 0<= i < N and 0<= j < N and matrix[i][j] == 1: # 탐색하는 곳에 집이면
        matrix[i][j]= 0 # 방문했다는 체크를 한다.
        unit_danji+=1
        danji_dfs(matrix,i-1,j)
        danji_dfs(matrix,i+1,j)
        danji_dfs(matrix,i,j-1)
        danji_dfs(matrix,i,j+1)

unit_danji = 0 #단지 내에 집이 몇개있는지
danji_list = [] # 단지 수 넣을 배열
count  = 0 # 총 단지수

for i in range(N):
    for j in range(N):
        if  matrix[i][j] == 1: # 탐색하는 곳이 집이면 거기부터 탐색 시작
            danji_dfs(matrix,i,j)
            count+=1
            danji_list.append(unit_danji)
            unit_danji = 0

print(count)
for num in sorted(danji_list):
    print(num)