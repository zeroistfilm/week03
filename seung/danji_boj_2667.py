import sys
sys.stdin = open("./seung/input.txt","r")
n= int(input())
matrix = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

print("처음:")
for row in matrix:
    print(row)
print("-----")
count = 0
danji_unit = 0
danji_lst = []
def danji_dfs(matrix,i,j):
    global count,danji_unit
    if 0<= i < n and 0 <= j < n and matrix[i][j] == 1:
        danji_unit += 1
        matrix[i][j] = 0
        danji_dfs(matrix, i-1, j)
        danji_dfs(matrix, i+1, j)
        danji_dfs(matrix, i, j-1)
        danji_dfs(matrix, i, j+1)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            danji_dfs(matrix,i,j)
            count += 1
            danji_lst.append(danji_unit)
            danji_unit = 0

print(count)
for item in sorted(danji_lst):
    print(item)